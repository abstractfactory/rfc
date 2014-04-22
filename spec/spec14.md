# Temporal Open Metadata

An extension to Open Metadata to support the notion of past, present and future.

![](https://dl.dropbox.com/s/3b09g8gl4y3is9u/spec14_tom_place_v001.png)

* Name: http://rfc.abstractfactory.io/spec/14
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: RFC1
* State: draft

Copyright, Change Process and Language is derived via inheritance as per RFC1.

# Goal

This document describes a method of making changes to metadata non-destructive; meaning that any change can be undone, redone and found at any point in time without affecting the overall interactivity and intuitiveness of operation. It does so by appending the following objects to the Open Metadata object-model:

* `history`
* `version`
* `imprint`
* `event`
* `trash`

And the following API functions:

* `history`
* `restore`

```python
dataset = om.metadata('/home/marcus', 'age')

# Get closest history
imprint = om.history(dataset).next()

# Restore to closest history
om.restore(imprint)

# *Note: Restoring to closest history will
# 		 in effect undo the latest change.
```

# Architecture

A `Group` is added to each metadata hierarchy.

```
folder
|--- .meta
	 |--- .history
	 |--- .versions
```

Within `history` lies versions of previously altered data; `imprints`. Each `imprint` contains information about when the change occured, who performed it as well as the previous value itself.

`version` is identical to `history` except that it is incrementally versioned and not concerned with time.

### Recorded history

Whenever an existing attribute is overwritten, a copy of it MAY be backed up. This backup MAY be retrievable at a later time and MAY feature support for persistent, per-user undo/redo.

#### Tracking on/off

The decision whether or not to record history MUST be offered as an option to the user; e.g. via the presence of a `track_history` null in the meta-metadata (more about meta-metadata in RFC15) of a given node. Or `do_not_track_history` depending on whether or not history should be tracked per-default or remain optional.

Recorded information

* Previous value
* Time
* User

Example

```
folder
|--- .meta
     |--- .history
     |    |--- some data&20140401-140541-604
     |    |    |--- user
     |    |    |--- value
     |    |--- some data&20140401-140751-121
     |    |    |--- user
     |    |    |--- value
     |    |--- some data&20140401-140751-126
     |         |--- user
     |         |--- value
     |--- some data
```

### An historical event

Each change MUST be recorded as an `event` containing the following information:

* Author
* Action taking place
* Path to target
* Summary of previous value
* Summary of current value
* Time

```
# Metadata layout example
folder
|---.meta
    |---.event  # <-- event `Dataset`

# Event contents
time
|--- author
|--- action
|--- metadata
|--- summary_current
|--- summary_previous

# Event contents Example
20140402-215327-643
|--- marcus
|--- modified
|--- parent/age.int
|--- 5
|--- 6

20140402-215345-643
|--- status.bool
|--- modified
|--- True
|--- False
|--- albert

```

As history may be discarded upon retrieval, it is important to retain some notion of history for future reference. For instance, multiple changes may have been made, but at some point in time a very early version of history was restored and thus discarded all following history. For users in the future, they would have no way of knowing whether there was any data between the restoration and previously latest value.

#### Preserving type

History MUST maintain the type of each value stored. E.g. when editing a `int`, making it a `float`, history MUST accurately preserve the change in type.

##### Example

```python
folder
|--- .meta
     |--- .history
     |    |--- age&20140401-100101-000  # <-- notice
     |    |    |--- user.string
     |    |    |--- value.int
     |    |--- age&20140401-100102-000  # <-- notice
     |    |    |--- user.string
     |    |    |--- value.float
```

Notice how "age" doesn't include a suffix? In this case, history stores the variable regardless of its type, and thus changing type would keep incrementing the same imprint. The value however is stored with type maintained.

### An alternative version

At any point in time MAY a node be stored as a version. A version is identical to a historical backup, except for its incremental versioning and that it may also support additional metadata such as a note.

Versions are useful when making changes that are hard to test without altering original data. A version could then be made, knowing that one could safely return at any point in time.

A note is stored as convenience for a future self or others who might be interested in knowing what has already been tried in before.

Recorded information

* Previous value
* Time
* User
* Note

Example

```python
|-- folder
|   |-- .meta
|   |   |-- .versions
|   |   |   |-- some data&v001
|   |   |   |   |-- user
|   |   |   |   |-- note
|   |   |   |   |-- previous_value
|   |   |-- some data.string
```

### Taking out the trash

Any removed node MUST be put into a persistent `trash` repository within its immediate parent.

```python
|-- folder
|   |-- .meta
|   |   |-- some data.string  # <-- remove
```

```python
|-- folder
|   |-- .meta
|   |   |-- .trash
|   |   |   |-- some data.string
```

Names of nodes - i.e. excluding their suffix - in trash MUST be unique; e.g. if "some data.string" is deleted, created once more as "some data.int" and again deleted, the first trashed node MUST be permanently deleted.

Target usage of trash is of software using it to either purposefully restore lost metadata or to casually suggest restoring metadata upon creation of new node that may already exist in trash.

### Undo

```python
>>> om.undo(item, user=None)
```

When there is history, there is the possibility of undoing changes made. Since anyone may make edits, there is the possibility of you undoing someone elses change.

```python
|-- .history
|   |-- some data.string&20140401-000000-001  # <-- by me
|   |-- some data.string&20140401-000000-002  # <-- by you
|   |-- some data.string&20140401-000000-003  # <-- by me
```

When specifying a `user` and the change about to be undone doesn't match Open Metadata MUST break operation and either raise an exception or return an error code.

### Redo

For every undo made, history is moved into a temporary '.redo' cache.

```python
|-- .history
|-- .redo
|   |-- some data.string&20140401-000000-001  # <-- time of undo
```

Original time-stamp is removed and replaced with the time of undoing so as to keep track of which to redo in which order.

Once new history is written, e.g. a new change has been made, the redo cache is permanently cleared.
