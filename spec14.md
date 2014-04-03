# Temporal Open Metadata (TOM)

An extension to Open Metadata to support the notion of past, present and future.

![](https://dl.dropbox.com/s/3b09g8gl4y3is9u/spec14_tom_place_v001.png)

* Name: https://github.com/abstract-factory/rfc/spec:14 (14/TOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: RFC1
* State: draft

Copyright, Change Process and Language is derived via inheritance as per [RFC1][].

# Goal

This document describes a method of making changes to metadata non-destructive by appending the following objects to the Open Metadata object-model:

* `history`
* `version`
* `imprint`
* `event`

# Architecture

A folder is added to each metadata hierarchy.

```python
+-- folder
|   +-- .meta
|   |   |-- .history
|   |   |-- .versions
```

Within `history` lies versions of previously altered data; `imprints`. Each `imprint` contains information about when the change occured, who performed it as well as the previous value itself.

`version` is identical to `history` except that it is incrementally versioned and not concerned with time.

### Recorded history

Whenever an existing attribute is overwritten, a copy of it is backed up. This backup may be retrieved at a later time and may feature support for persistent, per-user undo/redo.

Recorded information

* Previous value
* Time
* User

Example

```python
+-- folder
|   +-- .meta
|   |   +-- .history
|   |   |   +-- some data.string&20140401-140541-604
|   |   |   |   +-- user
|   |   |   |   +-- previous_value
|   |   |   +-- some data.string&20140401-140751-121
|   |   |   |   +-- user
|   |   |   |   +-- previous_value
|   |   |   +-- some data.string&20140401-140751-126
|   |   |   |   +-- user
|   |   |   |   +-- previous_value
|   |   +-- some data.string
```

### An historical event

Each change MAY be recorded as an `event` containing the following information:

* Action taking place
* Summary of previous value
* Summary of current value
* Time
* User

```python
# Folder layout
+-- folder
|   +-- .meta
|   |   +-- .event  # <-- event `file`

# Event contents
[time]
	[metadata]
	[action]
	[summary_previous]
	[summary_current]
	[user]

# Example
20140402-215327-643
	parent/age.int
	modified
	5
	6
	marcus

20140402-215345-643
	status.bool
	modified
	True
	False
	albert
```

As history may be discarded upon retrieval, it is important to retain some notion of history for future reference. For instance, multiple changes may have been made, but at some point in time a very early version of history was restored and thus discarded all history before it. For users in the future, they would have no way of knowing whether there was any data between the restoration and previously latest value.

### An alternative version

At any point in time MAY an attribute be stored as a version. A version is identical to a historical backup, except for its incremental versioning and that it may also support additional metadata such as a note.

Versions are useful when making changes that are hard to test without altering original data. A version could then be made, knowing that one could safely return at any point in time.

A note is stored as convenience for a future self or others who might be interested in knowing what has already been tried in before.

Recorded information

* Previous value
* Time
* User
* Note

Example

```python
+-- folder
|   +-- .meta
|   |   +-- .versions
|   |   |   +-- v001&some data.string
|   |   |   |   +-- user
|   |   |   |   +-- note
|   |   |   |   +-- previous_value
|   |   +-- some data.string
```

### Undo

```python
>>> om.undo(item, user=None)
```

When there is history, there is the possibility of undoing changes made. Since anyone may make edits, there is the possibility of you undoing someone elses change.

```python
+-- .history
|   +-- some data.string&20140401-000000-001  # <-- by me
|   +-- some data.string&20140401-000000-002  # <-- by you
|   +-- some data.string&20140401-000000-003  # <-- by me
```

When specifying a `user` and the change about to be undone doesn't match Open Metadata MUST break operation and either raise an exception or return an error code.

### Redo

For every undo made, history is moved into a temporary '.redo' cache.

```python
+-- .history
+-- .redo
|   +-- some data.string&20140401-000000-001  # <-- time of undo
```

Original time-stamp is removed and replaced with the time of undoing so as to keep track of which to redo in which order.

Once new history is written, e.g. a new change has been made, the redo cache is permanently cleared.

