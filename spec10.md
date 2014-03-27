# Arbitrary Open Metadata Hierarchy

This document describes the requirements involved in the next-generation of Open Metadata referred to as OM.2 in this specification; previous version referred to as OM.1

![](https://dl.dropbox.com/s/av2x8gel580ow48/om2_hierarchy.png)

* Name: https://github.com/abstract-factory/rfc/spec:10 (10/AOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:1

Copyright, Change Process and Language is derived via inheritance as per [spec:1][]

# History

As this is the first specification for Open Metadata, let us start with some background. Open Metadata was first initiated in 2013 to facilitate for the development of [Pipi][] and as a response to the ever-more complex nature of metadata in visual effects environments.

In these environments, metadata is crucial but often complicated and restricted. C

Complicated in that the way to interact with it is either via a web front-end, such as Shotgun of FTrack, or code. There is no connection between how users normally interact with data; i.e. using files and folders. Restricted because due to the limitations in how users interact with it the data-types you may assign as metadata are limited to mostly text and numbers. The amount of metadata may even be limited to the amount of available "fields" or to the dimensions of a textbox. But perhaps the largest limitation is that you are only capable of assigning metadata to pre-defined objects.

Before we more on, let's define what exactly metadata and its big brother metacontent means.

* meta -- Pertaining to a level above or beyond
* content -- A collection of data
* data -- A piece of information

So it would seem content is merely a container for data, and that `meta` represents a higher-level view of both.

And as opposed 

Reference
* [Notes on consistent metadata][]
* [Introduction to Augment pt. 1][]
* ["Everything is a file"][]

# Goal

Break free from the 2-level hierarchy imposed by OM.1 and support hierarchies of an arbitrary depth and width.

[spec:11][] (Miller Columns) defines a hierarchical representation of data that encourages the use of metadata in any situation. This is different from the current OM.1 in which data is forced into a 2-level hierarchy of `channel` and `key`. The goal of this spec then is to make Open Metadata compatible with [spec:11][].

# Proposal

Regular folders have representation, use and established syntax.

* `separator` + (`name` + `suffix`) = `separator + `basename`
* `\` + `funny_picture` + `.jpeg` = `\` + funny_picture.jpeg`

A path then is made up out of one or more `basename` objects, each preceeded by `separators`. If this layout could be perceived as two-dimensional, `x` and `y` where `x` represents a path (i.e. location) and `y` the content at that path - then Open Metadata represents a third-dimension `z`, an alternate to `y`.

Their configuration might look as follows:

`x`/`y` --> `location`/`content`

`x`/`z` --> `location`/`metadata`

Where `x`/`y` is data as seen via Windows Explorer and `x`/`z` as seen via About.

A file-system is a hierarchical and proven system proven in a vast array of scenarios; it is the purpose of this spec to tap into that resource and to further extend it.

# Architecture

Open Metadata defines three types; `location`, `group` and `dataset`. Location refers to the `x` from above; the absolute path to a folder on disk.

```python
location = '/home/marcus'
```

A group in metadata is the equivalent of a folder on disk and a dataset its file.

Groups, like folders, MAY contain one or more datasets and/or groups; a dataset on the other hand MUST NOT contain groups or other datasets.

### Data-types

A new concept introduced in OM.2 is the *data-type*. A data-format is the physical layout of one's and zero's within the one-dimensional array of bytes that make up a file on a file-system, e.g. `jpeg`, `zip`. A data-type however is their interface towards the programmer - their object-type, if you will - and determines what tools are available; both textually but also graphically.

Here are a few examples

* `dataset.bool`
* `dataset.int`
* `dataset.float`
* `dataset.string`
* `dataset.date`
* `group.enum`
* `group.tuple`
* `group.list`
* `group.set`

`bool`, `int`, `float`, `string` and `date` represent simple files with an added suffix corresponding to their type, such as *myfile.string*. `enum`, `tuple` and `list` however are different from regular groups in that they are *ordered*; meaning they maintain the individual indexes of each member. This is useful when storing data that may be visualised in a UI which needs to display items in a certain order; such as a full address.


```python
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

`set` represents a unique collection of datasets similar to what you would expect from a Python set, and `date` is essentially a `string` with special formatting.

### Data-formats

Native data-formats, such as `txt` or `jpeg` are treated with the minimal knowledge that their corresponding suffix allows, which in most cases are fine; a `jpeg` can only mean a rectangular bit-map with only one possible compression method.

### Location

Refer to an absolute path as *location* so as to facilitate for future expansion into using URI/URL addresses.

It MUST NOT matter to the programmer *where* the metadata is stored and it MUST NOT matter in what format that data resides. With such assumptions, we can assert valid metadata and standard use regardless of it residing on a remote file-system, within a binary file or in-memory within an application. Any content can contain metadata, regardless of what is hosting it.

### Writing to groups

Data MAY be written directly to groups; this becomes the metadata of that group. In the example above we write directly to a Group object. The resulting datasets are formatted according to the group's suffix which in this case results in an ordered list.

In other cases, where the group has no suffix, the data is formatted as-is; meaning OM.2 will determine in which format the data is to be stored based on its object-type within the given programming language and imprint the result into the suffix of the dataset.

```python
# Example of auto-determining data-type from suffix-less group
group = om.Group('mygroup', parent=location)
group.data = ['some data']
```

This MAY introduce a possible performance penalty; due to the amount of guess-work that has to be done and so the user SHOULD explicitly specify the data-type for any given group.

# Graphical Representation

Another major concern with OM.1 was how data was to be displayed in a graphical user interface. 

# Syntax

The purpose of Open Metadata remains the same and the syntactical differences are cosmetic-only.

```python
"""Demonstration of the previous syntax"""

import os 
import openmetadata as om 
  
# Determine where on disk to add metadata 
path = os.path.expanduser('~') 
path = os.path.join(path, 'test_folder') 
  
# Instantiate a Folder object 
folder = om.Folder(path) 
  
assert not folder.exists 
  
# Establish some data to write 
data = { 
    'hello': 'there', 
    'startFrame': 5, 
    'endFrame': 10, 
    'hidden': True
} 
  
# Channel objects represents a high-level data-type; 
# currently supported are: 
#   * kvs   -- Key/Value Store 
#   * txt   -- Plain Text 
#   * mdw   -- Markdown 
channel = om.Channel('keyvaluestore.kvs', parent=folder) 
  
# Inject data from above and write it out, missing 
# folders in the hierarchy are created automatically, 
# such as our `test_folder` 
channel.data = data 
channel.write() 
  
assert channel.data == data 
assert folder.data == {channel.name: data}
  
# Finally, remove our folder 
folder.clear() 
assert not folder.exists 

```

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

["Everything is a file"]: http://www.abstractfactory.io/blog/everything-is-a-file/
[Introduction to Augment pt. 1]: http://www.abstractfactory.io/blog/introduction-to-augment-pt-1/
[Notes on consistent metadata]: http://www.abstractfactory.io/blog/notes-on-consistent-metacontent/
[spec:1]: www.google.com
[spec:11]: www.google.com