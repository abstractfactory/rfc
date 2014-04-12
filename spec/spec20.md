# Metadata Referencing

This document describes methods for having one set of metadata be available from multiple locations.

![](../images/20/title.png)

* Name: http://rfc.abstractfactory.io/spec/20
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:1

Copyright and Language can be found in RFC1

# Goal

It can sometimes be useful to expose metadata from multiple locations; be it for storage-space concerns or simply for greater accessbility in a refined interface.

For example, it may become necessary to disjoint a hierarchy of nodes into two separate threads. Each thread containing a one duplicate of an identical node, yet both representing the same set of content.

The disjointing may be due to practical or logical concerns; in either case there is a need for a duplication of metadata. But, rather than naively copying and synchronising, one may `mirror` metadata so that they appear as one and the same. Now there is no longer any synchronisation and you can rest assured that no data falls out of sync.

# Architecture

For Open Metadata using the file-system, three objects are introduced:

* `symlink`
* `hardlink`
* `junction`

Each representing their corresponding file-system feature.

#### symlink

Symlink provides a de-coupled, potentially relative mapping between a file in one place and a file in another. It is the quickest and least obtrusive method of mirroring metadata and works across separate file-systems.

#### hardlink

A hardlink creates a new file pointing to the same byte-stream on disk as the original. Only possible with files on the same file-system, this method provides the most robust method of ensuring synchronisation between original and mirror and also ensures that data is available as long as there is at least one link to the byte-stream left.

#### junction

A junction provides features similar to hardlinks and features the same benefits, except it applies to folders instead.