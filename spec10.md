# Arbitrary Open Metadata Hierarchy

This document describes the requirements involved in the next-generation of Open Metadata referred to as OM.2 in this specification; previous version referred to as OM.1

![](https://dl.dropbox.com/s/av2x8gel580ow48/om2_hierarchy.png)

* Name: https://github.com/abstract-factory/rfc/spec:10 (10/AOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:1

Copyright, Change Process and Language is derived via inheritance as per [spec:1][]

# History

As this is the first specification for Open Metadata, let us start with some background. Open Metadata was first initiated in 2013 to facilitate for the development of [Pipi][] and as a response to the ever-more complex nature of meta-data for common use.

#### Definition

* meta -- Pertaining to a level above or beyond
* content -- A collection of data
* data -- A piece of information

#### More Reference

* [Notes on consistent meta-data][]
* [Introduction to Augment pt. 1][]
* ["Everything is a file"][]

# Goal - Open Metadata

The goal of Open Metadata is to introduce a mechanism with which to append meta-data to folders in such a way that it becomes as transparent to the end-user as handling files.

Meta-data is crucial and a basic component not only of computers and the systems we build, but to our psyche. Knowledge is knowledge, but so is our knowledge about this knowledge and therein lies the keyword; *about*. Meta-knowledge, and knowledge to a computer is called `data`.

Thus, Open Metadata MUST allow for any `data` to contain meta-data, including meta-data itself, and it must to so in a manner that doesn't affect the original `data` in any way and finally this data MUST NOT be bound by any particular representation; meaning it may be in the form of a True or False statement, a string or list of strings or quite simply any format capable of being represented on a file-system.

# Goal - OM.2

Break free from the 2-level hierarchy imposed by OM.1 and support hierarchies of an arbitrary depth and width.

[spec:11][] (Miller Columns) defines a hierarchical representation of data that encourages the use of meta-data in any situation. This is different from the current OM.1 in which data is forced into a 2-level hierarchy of `channel` and `key`. The goal of this spec then is to make Open Metadata compatible with [spec:11][].

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

Open Metadata defines three types; `location`, `group` and `dataset`. Location refers to the `x` from above; the absolute path to a folder on disk.

```python
location = '/home/marcus'
```

A group in meta-data is the equivalent of a folder on disk and a dataset its file.

Groups, like folders, MAY contain one or more datasets and/or groups; a dataset on the other hand MUST NOT contain groups or other datasets.

### Data-types

A new concept introduced in OM.2 is the *data-type*. A data-format is the physical layout of one's and zero's within the one-dimensional array of bytes that make up a file on a file-system, e.g. `jpeg`, `zip`. A data-type however is their interface towards the programmer - their object-type, if you will - and determines what tools are available; both textually but also graphically.

Here are a few examples

* `dataset.bool`
* `dataset.int`
* `dataset.float`
* `dataset.string`
* `dataset.date`
* `dataset.null`
* `group.enum`
* `group.tuple`
* `group.list`

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
group.write()

assert group.data == data

```

### Data-formats

Native data-formats, such as `txt` or `jpeg` are treated with the minimal knowledge that their corresponding suffix allows, which in most cases are fine; a `jpeg` can only mean a rectangular bit-map with only one possible compression method.

### Location

Refer to an absolute path as *location* so as to facilitate for future expansion into using URI/URL addresses.

It MUST NOT matter to the programmer *where* the meta-data is stored and it MUST NOT matter in what format that data resides. With such assumptions, we can assert valid meta-data and standard use regardless of it residing on a remote file-system, within a binary file or in-memory within an application. Any content can contain meta-data, regardless of what is hosting it.

### Writing to groups

Data MAY be written directly to groups; this becomes the meta-data of that group. In the example above we write directly to a Group object. The resulting datasets are formatted according to the group's suffix which in this case results in an ordered list.

In other cases, where the group has no suffix, the data is formatted as-is; meaning OM.2 will determine in which format the data is to be stored based on its object-type within the given programming language and imprint the result into the suffix of the dataset.

```python
# Example of auto-determining data-type from suffix-less group using
group = om.Group('mygroup', parent=location)
group.data = ['some data']
```

This MAY introduce a possible performance penalty; due to the amount of guess-work that has to be done and so the user SHOULD explicitly specify the data-type for any given group.

#### Meta-meta-data

It may sometimes be necessary to assign meta-data to meta-data itself; for example, the group.list type represents a physical folder on disk with the suffix ".list"

```python
- personal.list
  |-- firstname.string
  |-- lastname.string
  |-- age.int
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
  |-- __order__
  |-- firstname.string
  |-- lastname.string
  |-- age.int
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
group.write()
  
assert group.data == data
assert location.data == {group.name: data}

location.clear()
assert not location.exists
```

## \__call__

As an alternative to `dataset.read()` one may simply call upon a `group` or `location` object, using a path as argument.

```python
>>> location = om.Location('/home/marcus')
>>> group = location('/description')
>>> print group('/firstname')
'Marcus'
```

Sure reduces the number of lines, but perhaps not terribly intuitive.

## The use of write()

Coupling reading and writing within the same object sure is a convenience, but it introduces a security risk. I'm not talking about someone hacking your object while you use it, but more of security for you while using it. Having write() so close to overall operation of an object, a misspelling or misuse could potentially lead to removing important information.

An alternative is to introduce a separate method responsible for write-operations.

```python
>>> location = om.Location('/home/marcus')
>>> group = om.Group('description.list')
>>> group.data = ['my', 'ordered', 'list']
>>> om.write(group)
```

It didn't take any more lines of code, yet the implementation of writing is de-coupled from the object with which the contains resides and put into a more global space from where it can be distributed appropriately if need be.

# Distribution and Concurrent reads

Your operating system is very adapt at distributing the tasks you assign to it. However there are times when even the smartest operating system with the smartest of hard-drives can corrupt your data; it is after all, the real world.

One possible source of this corruption is multiple writes to a single location. Since Open Metadata is all about collaborative edits, how can it ensure that data is never written from one location while at the same time being written from another?

One possibly solution is to introduce a `broker`.

![](https://dl.dropbox.com/s/gyqptp90bjno20x/pep10_concurrency.png)

It would then be up to the `broker` to delegate or queue requests to the best of a file-systems capabilities; possibly guaranteeing that there is at most only ever a single writing operating taking place at any given moment per physical hard-disk.

# Arbitrary Depths

An important aspect of OM.2 is that of arbitrary depths; i.e. allowing for an unlimited nesting of `dataset` within `group`.

```python
|-- top folder
|   |-- group1
|   |   |-- group2
|   |   |   |--group3
|   |   |   |   |-- dataset.string

|-- top folder
    |-- group1
        |-- group2
            |--group3
                |-- dataset.string
```

[Pipi]: http://pipi.io
["Everything is a file"]: http://www.abstractfactory.io/blog/everything-is-a-file/
[Introduction to Augment pt. 1]: http://www.abstractfactory.io/blog/introduction-to-augment-pt-1/
[Notes on consistent meta-data]: http://www.abstractfactory.io/blog/notes-on-consistent-metacontent/
[spec:1]: www.google.com
[spec:11]: www.google.com