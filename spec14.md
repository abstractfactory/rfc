# Temporal Open Metadata (TOM)

An extension to Open Metadata to support the notion of temporal data; e.g. history and versions.

![](https://dl.dropbox.com/s/3b09g8gl4y3is9u/spec14_tom_place_v001.png)

* Name: https://github.com/abstract-factory/rfc/spec:14 (14/TOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: RFC1
* State: draft

Copyright, Change Process and Language is derived via inheritance as per [RFC1][].

# Goal

In a collaborative environment, things change. This document describes a method of making metadata changes non-destructive. We do this by appending `history` `version` and `imprint` to the Open Metadata arsenal.

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

### History

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
|   |   |   +-- 20140401-140541-604&some data.string
|   |   |   |   +-- user
|   |   |   |   +-- previous_value
|   |   |   +-- 20140401-140751-121&some data.string
|   |   |   |   +-- user
|   |   |   |   +-- previous_value
|   |   |   +-- 20140401-140751-126&some data.string
|   |   |   |   +-- user
|   |   |   |   +-- previous_value
|   |   +-- some data.string
```

### Versions

At any point in time may an attribute be stored as a version. A version is identical to a historical backup, except for its incremental versioning and that it may also support additional metadata such as a note.

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
|   |   |   +-- r001&some data.string
|   |   |   |   +-- user
|   |   |   |   +-- note
|   |   |   |   +-- previous_value
|   |   +-- some data.string
```