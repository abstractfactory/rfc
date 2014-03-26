# Arbitrary Open Metadata Hierarchy

This document describes the requirements involved in the next-generation of Open Metadata referred to as OM.2 in this specification.

![](https://dl.dropbox.com/s/av2x8gel580ow48/om2_hierarchy.png)

* Name: https://github.com/abstract-factory/rfc/spec:10 (10/AOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:1

Copyright, Change Process and Language is derived via inheritance as per [spec:1][]

# Goal

[spec:11][] defines a hierarchical representation of all data, encouraging the use of metadata at any level. This is different from the current Open Metadata v.1 in which data is forced into a 2-level hierarchy of `channel` and `key`. The goal of this spec then is to make Open Metadata compatible with [spec:11][].

# Proposal

Regular folders have representation, use and established syntax.

`separator` + `name` +`extension`

If this layout could be perceived as two-dimensional, `x` and `y` - `x` being their absolute path (i.e. location) and `y` their content - then Open Metadata represents a third-dimension `z`, an alternate to `y`.

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

A new concept introduced in OM.2 is the *data-type*. A data-format is the physical layout of one's and zero's within the one-dimensional array of bytes that make up a file on a file-system. A data-type however is their interface towards programmer - their object-type, if you will - and determines which tools are available; both textually but also graphically.

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

`bool` till `date` represent simple files with an added suffix corresponding to their type, such as *myfile.string*. `enum`, `tuple` and `list` however are different from regular groups in that they are *ordered*; meaning they maintain the individual indexes of each member. This is useful when storing data that may be visualised in a UI which needs to display items in a certain order; such as a full address.


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

Native data-formats, such as `txt` or `jpeg` are treated with the minimal knowledge that their corresponding suffix allows, which in most cases are fine; a `jpeg` can only mean a rectangular bit-map with only one possible compression method. A `txt` however may be formatted in markdown, there is no way for OM.2 to know.

### Location

Refer to an absolute path as *location* rather than *path* so as to facilitate for future expansion into using full URI/URL addresses.

It MUST NOT matter to the programmer where the metadata is stored and it MUST NOT matter in what format that data resides. This makes it possible to assert valid metadata and standard use of said metadata regardless of it residing on a remote file-system, within a binary file or in-memory within an application. Any content can contain metadata, regardless of what is hosting it.

```python
group = om.Location('/home/marcus')
metadata = group.read('/system/hidden')
```

[spec:1]: www.google.com
[spec:11]: www.google.com