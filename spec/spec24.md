# Methods of storing metadata

This document describes all possible methods of storing metadata.

* Name: http://rfc.abstractfactory.io/spec/24
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC23, RFC25, RFC27, RFC39

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

Associating metadata with content is paramount in digital asset management. There are a few solutions out there which facilitates this; in this spec we'll have a look at some of these and talk a little bit about why we at Abstract Factory chose to roll our own.

# Existing solutions deemed unsuited

History is packed full of attempts at associating content with metadata; each of which was deemed unsuited to the goals of Pipi. More information about these goals can be found in RFC25.

Why exactly were these methods deemed unsuited? Let's go through each possible method at a higher level.

### Piggyback metadata

```python
  ___________
 |           |\        ____   # Data added to existing data
 |           _|      _|    |
 |          |       | |    |
 |          |  <--  | | +  |
 |          |_      |_|    |
 |            |       |____|
 |____________|    

```

Piggyback is defined as

> "a ride on someone's back and shoulders"

Files and folders contain metadata, both explicit and implicit. Implicit metadata are things such as size, type and last modified dates. Those are indeed interesting and useful, but perhaps more interesting and useful are explicit metadata.

Explicit metadata is data in addition to data; i.e. the location of that photograph you took or the album cover of that mp3 you listened to. Neither are the content itself, they are both *about* the content.

There are a number of ways in which to store this type of metadata; such as XMP and ID3.

* [XMP][] --  First developed by [Adobe][] in 2001 and mainly used for images.
* [ID3][] -- Developed by [Damaged Cybernetics][] in 1996 and mainly used for audio; most prevalently perhaps the MP3 file-format.

XMP, ID3 and others are *explicit* metadata in that they append bits onto an existing file that host metadata. They both share one great weakness; they rely on whatever software reading the file to be aware of the existance of metadata; regardless of whether they make use of it or not - e.g. ID3 occupies a tiny space in the header of music files. Players not familiar with this metadata would play rather than discard the metadata and thus produce a short noise at the start of any song.

ID3 is a fixed-sized addition of metadata. It means you they only provide a certain amount of options, as well as a certain size of each option, and a total size of each - 30 bytes.

##### XML

Different from both XMP and ID3 in that, rather than enforcing itself into the very definition of a file-format, XML metadata lives happily together with any unicode content. Besides also being a file-format, it defines a method of adding metadata within a text-document via the use of `tags`.


```xml
<header>
  Some header content
  tagged with metadata
</header>
```

Here, the content "Some header content.." has been `tagged` with "header", indicating some information *about* the content; in this case that it is a header.

### Ad-hoc metadata

```python
  ___________
 |           |\
 |            |
 |            |
 |            |
 |            |
 |        # + |
 |____________|

```

A variant of piggyback metadata in which metadata is added within the augmented file directly - similar to XML. It is however bound to formats which support arbitrary modifications without having those affect the original content.

Some examples where this is possible;

* Nuke -- scene files stored in plain-text formats and allows for comments. Within each comment lies the potential of arbitrary data to be interpreted by an outside vendor.
* Maya -- may store scene files in plain-text as well.
* Sublime -- configuration files, plain-text

### Sidecar files

```python
  ____________
 |           |\       _______
 |            |      |      |\
 |            |      |   +   |
 |            |\  ___|_______|___
 |            | \|               |
 |            |  |_______________|
 |____________|     \_/     \_/

```

Sidecar files is defined as

> "files storing data not supported by the source file format"

Different from piggyback metadata in that, rather than a fusion of two separate formats, sidecar files remain separate to the data it augments.

This is the method used by [Open Metadata][] and in effect [Pipi][].

### Relational database

```python
  ____________
 |           |\                       _______
 |            |                      |      |\
 |            |                      |   +   |
 |            |                   ___|_______|___
 |            |< - - - - - - - - |               |
 |            |                  |_______________|
 |____________|                     |__|   |__| 
                                     \/     \/
```

By far the most common approach of storing metadata associated to content is with a relational database. In a relational database, metadata is stored, similar to sidecar files above, separate to the content it augments.

Content and metadata is then associated via a `relation` - most commonly in the form of an absolute path to the content on a file-system.

```
                                               attribute
                                          ___________________
                                         /                   \
         ___________________________________________________________
        |                       |       |                     |     |
        |         path          |  tag  |     description     | ... |
        |_______________________|_______|_____________________|_____|
      / |                       |       |                     |     |
tuple | | /path/to/content.jpeg | mytag | my long description | ... |
      \ |_______________________|_______|_____________________|_____|

         \_______________________ relation ________________________/

```

Each `attribute` capable of storing arbitrary data - most commonly strings - each providing a value for its corresponding key stored in the up-most row.

This is the method used by [Shotgun][], [FTrack][] and others.

### Graph Database

```python
  ____________
 |           |\                       _______
 |            |                      |      |\
 |            |                      |   +   |
 |            |                   ___|_______|___
 |            |< - - - - - - - - |               |
 |            |                  |_______________|
 |____________|                     |__|   |__| 
                                     \/     \/
```

Similar to Relational Databases, but with a different technology hosting content and the associated pros and cons that comes with that. Sadly I know very little of graph databases, someone else is free to fill in for me here.

### [HDF5][]

Not strictly designed for metadata, but useful as sidecar files and may contain arbitrary data in a well-insulated binary file-format.

### [Camlistore][]

I'm only familiar with the name, including it due to its potential relevance in storing metadata.

[Camlistore]: https://camlistore.org/
[Pipi]: http://abstractfactory.io/pipi
[HDF5]: http://www.hdfgroup.org/HDF5/
[Open Metadata]: https://github.com/abstractfactory/openmetadata
[Shotgun]: http://shotgunsoftware.com/
[FTrack]: https://www.ftrack.com/
[Adobe]: http://www.adobe.com
[ID3]: http://en.wikipedia.org/wiki/ID3
[XMP]: https://www.adobe.com/products/xmp/
[Damaged Cybernetics]: http://patpend.net/articles/ar/damaged.html
[defined by Wikipedia]: http://en.wikipedia.org/wiki/Sidecar_file