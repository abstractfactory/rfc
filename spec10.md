# Arbitrary Open Metadata Hierarchy

This document describes the requirements involved in the next-generation of Open Metadata referred to as mark 2 (Mk2) in this specification; previous version referred to as mark 1 (Mk1)

![](https://dl.dropbox.com/s/av2x8gel580ow48/om2_hierarchy.png)

* Name: https://github.com/abstract-factory/rfc/RFC10 (10/AOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: RFC1

Copyright, Change Process and Language is derived via inheritance as per [RFC1][]

# History

Open Metadata was first initiated in 2013 to facilitate the development of [Pipi][] and as a response to the ever-more complex nature of meta-data for common use.

#### Definition

* meta -- Pertaining to a level above or beyond
* content -- A collection of data
* data -- A piece of information

In layman's terms; "data about data" - regardless of data-type or traditional use.

#### References

* [Notes on consistent meta-data][]
* [Introduction to Augment pt. 1][]
* ["Everything is a file"][]

# Goal - Open Metadata

The goal of Open Metadata is to introduce a mechanism with which to append meta-data to folders in such a way that it becomes as transparent to the end-user as handling files.

Meta-data is crucial and a basic component not only of computers and the systems we build, but to our psyche. Knowledge is knowledge, but so is our knowledge about this knowledge and therein lies the keyword; *about*. Meta-knowledge, and knowledge to a computer is called `data`.

Thus, Open Metadata MUST allow for any `data` to contain meta-data, including meta-data itself, and it must to so in a manner that doesn't affect the original `data` in any way and finally this data MUST NOT be bound by any particular representation; meaning it may be in the form of a True or False statement, a string or list of strings or quite simply any format capable of being represented on a file-system.

# Goal - Mk2

Break free from the 2-level hierarchy imposed by Mk1 and support hierarchies of an arbitrary depth and width.

[RFC11][] (Miller Columns) defines a hierarchical representation of data that encourages the use of meta-data in any situation. This is different from the current Mk1 in which data is forced into a 2-level hierarchy of `channel` and `key`. The goal of this spec then is to make Open Metadata compatible with [RFC11][].

Another important evolution is separating the previous `File` and `Folder` objects into `Group` and `Dataset`. Too often did this cause confusion and conflict, both logically but also practically e.g. with the reserved variable name `file` in Python.

# Proposal

Regular folders have representation, use and established syntax.

* `separator` + (`name` + `suffix`) = `separator` + `basename`
* `\` + `funny_picture` + `.jpeg` = `\` + `funny_picture.jpeg`

A path then is made up out of one or more `basename` objects, each preceeded by a `separator`. If this layout could be perceived as two-dimensional where `x` represents a path and `y` representing the content at that path - then Open Metadata provides a third-dimension `z`, an alternate to `y`.

Their configuration might look as follows:

`x`/`y` --> `location`/`content`

`x`/`z` --> `location`/`meta-data`

Where `x`/`y` is data as seen via e.g. Windows Explorer and `x`/`z` as seen via e.g. About.

This third-dimension - or `tertiary` data - then extends upon the concept of a file-system in such a way that makes it possible to store, not only information in an explicit location within a hierarchy of information, but also information *about* this information, at any level, containing any number of additional levels.

# Architecture

Open Metadata defines four types; `location`, `group` and `dataset` and `blob`. Location refers to the `x` from above; the absolute path to a folder on disk.

```python
location = '/home/marcus'
```

A group in meta-data is the equivalent of a folder on disk and a dataset its file.

Groups, like folders, MAY contain one or more datasets and/or groups; a dataset on the other hand MUST NOT contain groups or other datasets.

Blobs are arbitrary data not necessarily understood by the Open Metadata library, such as `jpeg` or `mp3`.

### Data-types

A new concept introduced in Mk2 is the *data-type*. A data-format is the physical layout of one's and zero's within the one-dimensional array of bytes that make up a file on a file-system, e.g. `jpeg`, `zip`. A data-type however is their interface towards the programmer - their object-type, if you will - and determines what tools are available; both textually but also graphically.

Here are a all the supported types

* `dataset.bool`
* `dataset.int`
* `dataset.float`
* `dataset.string`
* `dataset.text`
* `dataset.date`
* `dataset.null`
* `group.enum`
* `group.tuple`
* `group.list`
* `group.dict`

`bool`, `int`, `float`, `string` and `date` represent simple files with an added suffix corresponding to their type, such as *myfile.string*. `enum`, `tuple` and `list` however are different from regular groups in that they are *ordered*; meaning they maintain the individual indexes of each member. This is useful when storing data that may be visualised in a UI which needs to display items in a certain order; such as a full address.


```python
# Python example
data = ['31 Quantum Tower',
    'Poland Road',
    'W21X 8SL',
    'London',
    'UK']

location = om.Location('/home/marcus')
group = om.Group('myaddress.list', parent=location)

group.data = data
group.commit()

assert group.data == data

```

### Data-formats

Native data-formats, such as `txt` or `jpeg` are treated with the minimal knowledge that their corresponding suffix allows, which in most cases are fine; a `jpeg` can only mean a rectangular bit-map with only one possible compression method.

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

### Revisions

At any point in time may an attribute be stored as a revision. A revision is identical to a historical backup, except that it allows for a note to be stored with it.

Revisions are useful when making changes that are hard to test without altering original data. A revision could then be made, knowing that one could safely return at any point in time.

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
|   |   +-- .revisions
|   |   |   +-- 20140401-140541-604&some data.string
|   |   |   |   +-- user
|   |   |   |   +-- note
|   |   |   |   +-- previous_value
|   |   +-- some data.string
```

### Location

Refer to an absolute path as *location* so as to facilitate for future expansion into using URI/URL addresses.

It MUST NOT matter to the programmer *where* the meta-data is stored and it MUST NOT matter in what format that data resides. With such assumptions, we can assert valid meta-data and standard use regardless of it residing on a remote file-system, within a binary file or in-memory within an application. Any content can contain meta-data, regardless of what is hosting it.

### Writing to groups

Data MAY be written directly to groups; this becomes the meta-data of that group. In the example above we commit directly to a Group object. The resulting datasets are formatted according to the group's suffix which in this case results in an ordered list.

In other cases, where the group has no suffix, the data is formatted as-is; meaning Mk2 will determine in which format the data is to be stored based on its object-type within the given programming language and imprint the result into the suffix of the dataset.

```python

# Example of auto-determining data-type from suffix-less group using
group = om.Group('mygroup', parent=location)
group.data = ['some data']
```

This MAY introduce a possible performance penalty; due to the amount of guess-work that has to be done and so the user SHOULD explicitly specify the data-type for any given group.

### Meta-meta-data

It may sometimes be necessary to assign meta-data to meta-data itself; for example, the group.list type represents a physical folder on disk with the suffix ".list"

```python
- personal.list
  +-- firstname.string
  +-- lastname.string
  +-- age.int
```

Lists are naturally ordered, but how can we store this order on disk together with the datasets it may contain? One way would be to introduce a header into each of the files.

```python
firstname.string = r'order=0\nMarcus'
```

This could potentially be appropriate in many situations, but would in this case introduce possibility of conflicting ordering. 

```python
firstname.string = r'order=2\nMarcus'
lastname.string = r'order=2\nOttosson'
```

So an alternative may be to store this information in a specially formatted dataset pertaining to the information at hand.

```python
- personal.list
  +-- __order__
  +-- firstname.string
  +-- lastname.string
  +-- age.int
```

```python
__order__ = r'firstname=0\nlastname=1\nage=2'
```

In code, meta-meta-data could then be retrieved as such:

```python
>>> location = om.Location('/home/marcus')
>>> firstname = location.read('/personal/firstname')
>>> type(firstname)
<type 'Dataset'>
>>> firstname.order
0
```

Each meta-meta-data dataset or group MAY be accessible via dot-notation syntax by languages that support it and MUST otherwise be accessible via other means.

If a dataset is not included in `__order__` then a null value MUST be returned. If the host group does not contain a `__order__` meta-meta-data set then an error MUST be raised.

# Syntax

The purpose of Open Metadata remains the same and the syntactical differences are cosmetic-only.

```python
"""Demonstration of the current syntax"""

import os 
import openmetadata as om 

path = os.path.expanduser('~') 
path = os.path.join(path, 'test_folder') 

location = om.Location(path) 
assert not location.exists 

data = {
    'hello': 'there', 
    'startFrame': 5, 
    'endFrame': 10, 
    'hidden': True
} 

group = om.Group('keyvaluestore.dict', parent=location)
group.data = data
group.commit()
  
assert group.data == data
assert location.data == {group.name: data}

location.clear()
assert not location.exists
```

### Dot-notation (deprecated)

Open Metadata MAY support the notion of accessing members via dot-notation syntax.

```python
location = om.Location('/home/marcus')

# Here, metadata is accessed via the group "personal" within the location
# followed by the dataset "firstname" residing within this group.
location.personal.firstname
'Marcus'
```

*Note*: This is not longer valid, as we use this to access meta-meta-data members.

### \__call__

As an alternative to `dataset.read()` one may simply call upon a `group` or `location` object, using a path as argument.

```python
>>> location = om.Location('/home/marcus')
>>> group = location('/description')
>>> print group('/firstname')
'Marcus'
```

Sure reduces the number of lines, but perhaps not terribly intuitive.

### Use of commit()

Coupling reading and writing within the same object sure is a convenience, but also introduces a security risk. I'm not talking about someone hacking your object while you use it, but more of security for you, yourself, while using an object. Having commit() so close to overall operation of an object, a misspelling or misuse could potentially lead to removing important information.

An alternative is to introduce a separate method responsible for commit-operations.

```python
>>> location = om.Location('/home/marcus')
>>> group = om.Group('description.list')
>>> group.data = ['my', 'ordered', 'list']
>>> om.commit(group)
```

It didn't take any more lines of code, yet the implementation of writing is de-coupled from the object with which the contains resides and put into a more global space from where it can be distributed appropriately if need be.

### Name conflicts

Due to Open Metadata referencing groups and datasets excluding their suffixes, there is the possibility of group `A.list` to hide the dataset `A.string`.

```python
>>> location = om.Location('/home/marcus')
>>> group = location.A  # Will we get the `list` or `tuple`?
```

It is up to the end-user to guarantee that names remain unique as there is no way for Open Metadata to enforce this constraint.

Open Metadata MAY constrain the adding of children to a parent when said child would hide an existing child.

```python
>>> location = om.Location('/home/marcus')
>>> group = om.Group('existing_group', parent=location)
ValueError: 'existing_group' already exists
```

However as meta-data may also be added ad-hoc via the file-system manually or via a third-part library Open Metadata is unable to enforce this constraint throughout.

As a result, only the first-returned item is visible to the end user. Open Metadata MAY provide a warning-message when the retrieved name is not unique.

Another area in which name-conflicts may happen is in the use of dot-notation for retrieving children. If a child occupies the same name as an existing member variable, such as 'data', then that child would NOT be accessible via dot-notation as member variables take precedence over children.

#### Example implementation

A graphical user interface could hinder the creation of groups and datasets that would end up hiding another group or dataset.

Alternatively, it may warn the user upon commit and suggest alternatives.

# Distribution and Concurrent Writes

> "If I write to file A, and you write to file A, who wins?"

Your operating system is very adapt at distributing the tasks you assign to it. However there are times when even the smartest operating system with the smartest of hard-drives can corrupt your data; it is after all, the real world.

One possible source of this corruption is multiple writes to a single location. Since Open Metadata is all about collaborative edits, how can it ensure that data is never written from one location while at the same time being written from another?

There are many ways of dealing with concurrency. Lets have a look at some in order of its increasing level of complexity.

### Introspection

Possibly the most straight-forward solution is to ash a file-system which files are currently in use and never try and write to one that is, but instead wait for it to become free. (lsof on linux, openfiles.exe on windows)

### Lock-files

Similar to Introspection, another (brute-force) approach of assuring that there is only ever one writer at a time is to use lock-files.

```python
+-- folder
|   +-- .meta
|   |   +-- data.string
|   |   +-- data.string.lock
```

A lock-file is merely an empty file somehow designating which files are "locked" for edits. When a lock-file exists, no other than the creator of the lock-file may edit the locked file.

Only upon completing the edit does the creator then remove his lock-file and thus restore permission for others to create lock-files of their own in preparation for their edits.

#### Lock-files and deadlocks

There is of course the possibility of an edit not completing successfully and thus leaving behind its lock-file. In these cases, the locked files are forever locked and can never be edited; not even to remove the lock-file.

In cases such as these it may be necessary to introduce a time-slot within which each edit is expected to take place. During edit, the editor could receive a heartbeat every so often - say 20 ms - to which the editor is required to respond. Upon failure to respond, the lock-file is automatically removed and the editor then looses permission to further write to this destination without re-establishing a lock-file.

### Broker

One possibly solution is to introduce a `broker`.

![](https://dl.dropbox.com/s/gyqptp90bjno20x/pep10_concurrency.png)

It would then be up to the `broker` to delegate or queue requests to the best of a file-systems capabilities; possibly guaranteeing that there is at most only ever a single writing operating taking place at any given moment per physical hard-disk.

#### RPC

One possible implementation of a broker is to utilising the Open Metadata library via proxy-methods such as a Remore Procedure Call (RPC).

Clients may call upon an exposed service pass to any data they wish to be written as Open Metadata through it. The recieving end would then manage the actual reads and writes to the file-system(s), thus ensuring that there is only ever one concurrent read and write happening while also being natively adept at queing requests and otherwise handle a gigantic amount of requests.

The broker then would be this service.

### Push/Pull

Similar to the Broker-model, another solution may be to write temporarily to one location, in preparation for the next.

![](https://dl.dropbox.com/s/ln3orzp5xldiz5q/spec10_pushpull.png)

```python
>>> location = om.Location('/server/location')
>>> dataset = om.Dataset('new_data.string', data='a value', parent=location)
>>> om.commit(dataset)
>>> om.push()
```

Here, a dataset is first "committed" to be written publicly, meaning it is written to the local hard-drive; in a common place for metadata written by this user.

```python
/home/marcus/.metastage/server/location/new_data.string
```

Upon om.push(), Open Metadata would look for ".metastage" underneath the calling user's home-directory and schedule that data to be written to a server.

The push-mechanism could then handle concurrency and decide who eventually ends up the latest writing the latest data, and also alert the user when writes happen within a certain time-span, such as within 0.1 microseconds. At that point, the user could reasonably expect his data to having been overwritten by someone else.

It could potentially also be the place where priorities are set on requests. Some users or processes may require their data to always take precedence over others, if that data should so happen to be written within a given time-span.

And ultimately, it would help guarantee that, even though data may be overwritten in one location, it is never lost and can be re-submitted either automatically or manually per a user's request.

### Push/Pull Daemon

One of the advantages over using a proxy for storage as opposed to working directly towards a database is that you can schedule for writes to happen at a time more convenient for writing.

For example, imagine you are working within an application which produces massive amounts of metadata; sporadically streaming to disk at a rate of 100mb/sec, and that it did so only for a few seconds.

If this data were to immediately write to a remote server, the transfer could potentially become a bottle-neck in this process.

Instead, the data could be written locally and a background process, a.k.a daemon, could then time the instances you are attempting to write and only Push once the time in between writes have reached a certain threshold; such as 10 seconds.

Only after 10 seconds of inactivity would the daemon get to work in pushing all of this data onto the server.

The user would get fast response-time, and the server would get one big chunk of data to store, rather than a sporadic cloud of requests.

# Arbitrary Depth

An important aspect of Mk2 is that of arbitrary depths; i.e. allowing for an unlimited nesting of `dataset` within `group`.

```python
+-- top folder
    +-- group1
        +-- group2
            +--group3
                +-- dataset.string
```

## Mixing `dataset` and `group`

Open Metadata MUST support the notion of mixing `dataset` and `group` objects within a hierarchy.

```python
+-- top folder
    +-- group1
    +-- dataset1
```

# Automatic types

Open Metadata MUST support the notion of lazily assigning data to `group` and `dataset` objects.

```python
>>> location = om.Location('/home/marcus')

# We'll define a dataset, but neglect to give it a suffix.
# The contents of this dataset could be anything at this point.
>>> dataset = om.Dataset('my_simple_dataset', parent=location)

# Assining data of type 'string' will automatically specify 'string' 
# as the data-type of this dataset, resulting in a file on disk with
# a suffix of 'string'
>>> dataset.data = 'my simple string'

>>> om.commit(dataset)
```

# Cascading (deprecated)

> Deprecation: This behavior was moved to [RFC12/OOM][]

Reading and writing MAY be cascading. Meaning data may be retrieved by query of a leaf-dataset, only to have data returned be influenc

For motivation and use of cascading data, head over to Steve Yegge's inspiration post about the [Universal Design Pattern][]

### Cascading reads

Open Metadata MUST support reading data recursively.

```python
# Picture this hierarchy

# +-- project
# |   +-- sequence
# |       +-- shot

>>> location = om.Location('/project/sequence/shot')
>>> executables = location.executables

# Now, it may be the case, that no executables reside
# within `shot`. However, in this environment, executables
# such as Maya or Houdini would typically reside within `project`

>>> print executables
{
  'maya': '/path/to/maya',
  'houdini': '/path/to/houdini'
}

# It may however be useful for these properties to "cascade" up
# through the hierarchy; eventually finding its way to us via the
# descendant `shot`
```

Why would we want this? Well, in addition to the specific points made by Steve in his post, we might want to support the notion of cascading data within a post-production environment in which each descendant may *add* or *subtract* from prior properties.

```python
# +-- project
# |   +-- sequence
# |       +-- shot

>>> project = om.Location('/project')
>>> project.executables
{
  'maya': '/path/to/maya',
  'houdini': '/path/to/houdini'
}

>>> shot = om.Location('/project/sequence/shot')
>>> shot.executables
{
  'maya': '/path/to/maya', 
  'houdini': '/path/to/houdini',
  'mari': '/path/to/mari'
}
```

In this example, `shot` has appended `mari` to its roster. It did so without duplicating the ascending hierarchy of metadata and by instead only adding `mari`. The cascading mechanism is then responsible for merging up-stream data.

Removing an existing entry is then as easy as:

```python
>>> shot.executables = {'maya': None}
```

### Cascading writes

Open Metadata MUST support the notion of commiting data to disk in a cascading manner.

```python
# Demonstration of a downwards commit, data located underneath
# committed object are also committed.
>>> location = om.Location('/home/marcus')
>>> group = om.Group('nested_data.list', parent=location)
>>> group2 = om.Group('sub_data', parent=group)
>>> dataset = om.Dataset('valid.bool', parent=group2)
>>> om.commit(location)  # <-- note `location`

# In an upwards commit, missing groups are automatically created
>>> location = om.Location('/home/marcus')
>>> group = om.Group('nested_data.list', parent=location)
>>> group2 = om.Group('sub_data', parent=group)
>>> dataset = om.Dataset('valid.bool', parent=group2)
>>> om.commit(dataset)  # <-- note `dataset`
```

# Native types

Open Metadata MUST support the addition of native OS data-types such as `jpeg` or `mov`. These files may not necessarily be viewable or even editable via the Open Metadata library, but still remains an important part of the possibilities facilitated by it.

## `blob`

When querying native data-types, Open Metadata MUST return an object of type `blob`. The functionality of `blob` objects are limited and MAY provide options for retrieving an absolute path, URL or URI.

```python
>>> location = om.Location('/home/marcus')
>>> image = location.reference_image
>>> type(image)
<type 'Blob'>
>>> image.path
'/home/marcus/.meta/reference_image.png'
>>> str(image)
'/home/marcus/.meta/reference_image.png'
```

# Esoteric types

In addition to what you would expect from a metadata-storage API, there is one other possibility that may keep you up at night (in a good way).

We'll cover

* `dataset.stream`
* `dataset.sql`
* `dataset.rpc`

### `stream`

```python
+-- folder
|   +-- presentation.stream
```

It's important to remember that a file is nothing more than a logical representation of a sequence of 1s and 0s on a hard-drive. Now, whenever you stream video from YouTube, this concept is still very much in play.

It may not stream to disk, but if it did it would not matter. What matters is the sequence of 1s and 0s and how those are represented to you.

In the example above, there is a dataset within a folder with the suffix 'stream'. This indicates that within this file lies instructions for how to connect to a source other than your hard-drive and to provide you with a handle to it; just like you would a regular file.

What do to with this handle however is outside of the scope of this specification and in fact outside the scope of Open Metadata itself.

What Open Metadata provides to you is the possibility of storing such an instruction in arbitrary folders on your hard-drive; it'd then be up to your front-end to interpret and possibly visualise this stream for you.

### `sql`

Any database is ultimately just one or more files on some disk. You could gain access to this file, but it would bear little meaning. What would be more interesting however is to attain a handle into a particular portion of an SQL-based database and manipulate it just like you would a regular Open Metadata dataset. Perhaps even store this handle somewhere in your local hard-drive, as metadata to a folder.

```python
>>> location = om.Location('/some/folder')
>>> location.tree()
# +-- folder
# |   +-- startFrame.sql
```

### `rpc`

How about reading and writing data via a remote procedure call (RPC)? The dataset could contain instructions for either and get interpreted by your application.

```python
>>> location = om.Location('/some/folder')
>>> location.tree()
# +-- folder
# |   +-- startFrame.rpc
```


[RFC12/OOM]: http://google.com
[universal design pattern]: http://steve-yegge.blogspot.co.uk/2008/10/universal-design-pattern.html
[Pipi]: http://pipi.io
["Everything is a file"]: http://www.abstractfactory.io/blog/everything-is-a-file/
[Introduction to Augment pt. 1]: http://www.abstractfactory.io/blog/introduction-to-augment-pt-1/
[Notes on consistent meta-data]: http://www.abstractfactory.io/blog/notes-on-consistent-metacontent/
[RFC1]: www.google.com
[RFC11]: www.google.com