# Arbitrary Open Metadata Hierarchy

This document describes the requirements involved in the next-generation of Open Metadata referred to as mark 2 (Mk2) in this specification; previous version referred to as mark 1 (Mk1)

![](https://dl.dropbox.com/s/av2x8gel580ow48/om2_hierarchy.png)

* Name: http://rfc.abstractfactory.io/spec/10
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Tags: publishing
* Related: RFC12, RFC13, RFC14, RFC15, RFC16, RFC17, RFC18, RFC20
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# History

Open Metadata was first initiated in 2013 to facilitate the development of [Pipi][] and as a response to the ever-more complex nature of metadata for common use.

#### Definition

* meta -- Pertaining to a level above or beyond
* content -- A collection of data
* data -- A piece of information

In layman's terms; "data about data" - regardless of data-type or traditional use.

#### References

* [Notes on consistent metacontent][]
* [Introduction to Augment pt. 1][]
* ["Everything is a file"][]

# Goal

Introduce a mechanism with which to associate metadata with a location in such a way that it becomes as transparent to the end-user as handling files.

Metadata is crucial and a basic component not only of computers and the systems we build, but to our psyche. Knowledge is knowledge, but so is our knowledge about this knowledge and therein lies the keyword; *about*. Meta-knowledge. Knowledge is information is `data`.

Open Metadata MUST allow for any `data` to contain metadata, including metadata itself, and it must to so in a manner that doesn't affect the original `data` (See RFC24 on "Sidecar files") and finally this data MUST NOT be bound by any particular representation; meaning it may be stored in any format capable of being represented on a file-system.

# Zen of Open Metadata

* Change is common
* Usability is more important than features
* Control is more important than performance
* Encapsulation is more important than disk space

<draft>
#### Cool isn't in technology but in how you use it

One of the things Open Metadata fights is the perception that "cool" equals "useful" and how new technology adds fuel to this fire.

Things like HDF5, Camlistore and ... each offer complex data management techniques out of the box and appeal to us in the same way magic appeals to laymen; thus the goal of Open Metadata is to encapsulate ALL of what is capable with HDF5, Camlistone and others using the most basic of techniques proven to work and guaranteed to last for the next couple of decennia.
</draft>

# Architecture

Open Metadata defines five types; `node`, `location`, `group` and `dataset` and `blob`. Location refers to the `x` from above; the absolute path to a folder on disk.

```python
location = '/home/marcus'
```

Nodes represent and entry in a `database` and is the supertype of all other objects. `database` may be anything from SQL to file-systems to in-memory data-structures.

A group in metadata is the equivalent of a folder on disk and a dataset a file.

Groups, like folders, MUST feature support for one or more datasets and/or groups; a dataset on the other hand MUST NOT contain groups or other datasets.

Blobs are arbitrary data not necessarily understood by the Open Metadata library, such as `jpeg` or `mp3` and are treated like incomprehensible blobs of data; usually either copied or hard-linked into a metadata repository.

Read more about Blobs in RFC16

### Data-types

A new concept introduced in Mk2 is the *data-type*. A data-format is the physical layout of one's and zero's within the one-dimensional array of bytes that make up a file on a file-system, e.g. `jpeg`, `zip`. A data-type however is their interface towards the programmer - their object-type, if you will - and determines what tools are available; both textually but also graphically.

Here are a all the supported types

**Generic**

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

**Numbers**

* `group.point`
* `group.vector`
* `group.matrix`

**Web**

* `dataset.email`
* `dataset.like`

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
group.dump()

assert group.data == data

```

### Default values

Each dataset MUST start out with a default value.

* `dataset.bool` = `False`
* `dataset.int` = `0`
* `dataset.float` = `0.0`
* `dataset.string` = `''`
* `dataset.text` = `''`
* `dataset.date` = `Current Date`
* `dataset.null` = `Empty`


### Data-formats

Native data-formats, such as `txt` or `jpeg` are treated with the minimal knowledge that their corresponding suffix allows, which in most cases are fine; a `jpeg` can only mean a rectangular bit-map with only one possible compression method.

### Location

Refer to an absolute path as *location* so as to facilitate for future expansion into using URI/URL addresses.

It MUST NOT matter to the programmer *where* the metadata is stored and it MUST NOT matter in what format that data resides. With such assumptions, we can assert valid metadata and standard use regardless of it residing on a remote file-system, within a binary file or in-memory within an application. Any content can contain metadata, regardless of what is hosting it.

### Writing to groups

Data MAY be written directly to groups; this becomes the metadata of that group. In the example above we dump directly to a Group object. The resulting datasets are formatted according to the group's suffix which in this case results in an ordered list.

In other cases, where the group has no suffix, the data is formatted as-is; meaning Mk2 will determine in which format the data is to be stored based on its object-type within the given programming language and imprint the result into the suffix of the dataset.

```python

# Example of auto-determining data-type from suffix-less group using
group = om.Group('mygroup', parent=location)
group.data = ['some data']
```

This MAY introduce a possible performance penalty; due to the amount of guess-work that has to be done and so the user SHOULD explicitly specify the data-type for any given group.

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
group.dump()
  
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

*Note*: This is not longer valid, as we use this to access meta-metadata members.

### \__call__ (deprecated)

As an alternative to `dataset.read()` one may simply call upon a `group` or `location` object, using a path as argument.

```python
>>> location = om.Location('/home/marcus')
>>> group = location('/description')
>>> print group('/firstname')
'Marcus'
```

Sure reduces the number of lines, but perhaps not terribly intuitive.

### Use of dump()

Coupling reading and writing within the same object sure is a convenience, but also introduces a security risk. I'm not talking about someone hacking your object while you use it, but more of security for you, yourself, while using an object. Having dump() so close to overall operation of an object, a misspelling or misuse could potentially lead to removing important information.

An alternative is to introduce a separate method responsible for dump-operations.

```python
>>> location = om.Location('/home/marcus')
>>> group = om.Group('description.list')
>>> group.data = ['my', 'ordered', 'list']
>>> om.dump(group)
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

However as metadata may also be added ad-hoc via the file-system manually or via a third-part library Open Metadata is unable to enforce this constraint throughout.

As a result, only the first-returned item is visible to the end user. Open Metadata MAY provide a warning-message when the retrieved name is not unique.

Another area in which name-conflicts may happen is in the use of dot-notation for retrieving children. If a child occupies the same name as an existing member variable, such as 'data', then that child would NOT be accessible via dot-notation as member variables take precedence over children.

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

>>> om.dump(dataset)
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


[Pipi]: http://pipi.io
["Everything is a file"]: http://www.abstractfactory.io/blog/everything-is-a-file/
[Introduction to Augment pt. 1]: http://www.abstractfactory.io/blog/introduction-to-augment-pt-1/
[Notes on consistent metacontent]: http://www.abstractfactory.io/blog/notes-on-consistent-metacontent/