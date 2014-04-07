# Pipi Metadata

This document describes the method with which Pipi reads and writes metadata.

* Name: http://rfc.abstractfactory.io/spec/25 (25/PRQ)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC23
* Tags:

Copyright, Change Process and Language can be found in [RFC1][]

# Goal

Coupling content with metadata is crucial in content management and there are a few alternatives out there that facilitate this; in this spec we'll have a look at some of these and talk a little bit about why Pipi instead chose to roll its own.

# Alternatives

There have been numerous attempts in the past at associating content with metadata; each of which was deemed unsuited to the goals of Pipi. More information about these goals can be found in [RFC25/Pipi Goals][] along with a definition of Metadata in [RFC26/What is Metadata][]

Why exactly were these methods deemed unsuited?

*Note: have a look at [RFC26][] for futher definition of how "metadata" is defined in Pipi.

### Piggyback metadata

Piggyback is defined as

> "a ride on someone's back and shoulders"

Files and folders contain metadata, both explicit and implicit. Implicit metadata are things such as size, type and last modified dates. Those are indeed interesting and useful, but perhaps more interesting and useful are explicit metadata.

Explicit metadata is data in addition to data; i.e. the location of that photograph you took or the album cover of that mp3 you listened. Neither are the content itself, they are both descriptions of content.

There are a number of ways in which to store this type of metadata; some of which are [XMP][] first developed by [Adobe][] in 2001 and mainly used for images and [ID3][] developed by [Damaged Cybernetics][] in 1996 and mainly used for audio; most prevalently perhaps the MP3 file-format.

XMP, ID3 and others are *explicit* metadata in that they append bits onto an existing file that host metadata. The two aspects they all share is perhaps also their greatest weaknesses

1. They rely on whatever software reading the file to be aware of the existance of metadata; whether they make use of it or not - e.g. ID3 occupies a tiny space in the header of music files. Players not familiar with this metadata would play rather than discard the metadata and thus produce a short noise at the start of any song.

2. The type and amount of metadata that each protocol support are fixed; either due to the amount of space they occupy - ID3 occupy exactly 30 bytes of space - or due to the standard imposing a certain set of entries assumed to be most commonly sought after - XMP supposedly supports binary but is most prevalently used to store text. [1](http://en.wikipedia.org/wiki/Extensible_Metadata_Platform)

### Ad-hoc metadata

- storing ad-hoc in maya ascii, nk and others

### Sidecar files

Sidecar files is defined as

> "files storing data not supported by the source file format"

As opposed to self-contained metadata, described above, this method allows for the storage of metadata with any item - file or folder - and doesn't pose any restrictions as to what data may be stored or in which way to store it.

- storing metadata as content, together with content.

### Relational database

By far the most common, sustainable approach of storing metadata in relation to content is with a relational database. In a relational database, content is stored as a reference - most commonly as paths absolute within given environment - and metadata as attributes

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

Each `attribute` capable of storing arbitrary data - most commonly strings - each providing a value to its corresponding key stored in the up-most row.

#### Pros

As all data is stored within a strict table, lookup is fast and facilitates complex search queries based on any combination of attributes.

#### Cons


### HDF5

[Adobe]: http://www.adobe.com
[ID3]: http://en.wikipedia.org/wiki/ID3
[XMP]: https://www.adobe.com/products/xmp/
[Damaged Cybernetics]: http://patpend.net/articles/ar/damaged.html
[defined by Wikipedia]: http://en.wikipedia.org/wiki/Sidecar_file