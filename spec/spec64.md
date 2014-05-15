# Programmable Content

Definition of what it means for content to be programmable.

* Name: http://rfc.abstractfactory.io/spec/64
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC65
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

Programmable Content is a data-driven method of storing content designed for automation. It substitutes much of:

* naming conventions
* database as data-store for metadata
* directory-structure dependency
* round-trip conventions (e.g. Users are at /home, and /home/Marcus is a User)

And serves as an alternative for:

* directory structure convention
* directory structure schema

Pre-requisites; intelligent content.

See also RFC65
See also [Unified Content Strategy](http://www.amazon.co.uk/Managing-Enterprise-Content-Unified-Strategy/dp/032181536X)

### Naming convention

What are the requirements of a naming convention, and why is naming convention so important to begin with?

In most cases, the one requirement can be distilled into one word - metadata.

```bash
$ /projects/hulk/shots/1000/hulk_1000_v001_marcus.ma
```

Here, the following metadata is embedded in this file `hulk_1000_v001_marcus.ma`:

* `hulk` Which project it belongs to
* `1000` Which shot it belongs to
* `v001` Which version it is
* `marcus` Who is to blame
* `ma` Format of the file

Accidental mis-placement of this file becomes obvious and, if adhered to, a file could safely be returned to its rightful directory.

```bash
# This file is clearly in the wrong place.
$ /projects/hulk/shots/1000/spiderman_1000_v001_marcus.ma
```

Let's refer to this type of integrity as `structural integrity`; a file is meant for a certain location within a hierarchy. If this file is moved, it could potentially break dependent files from finding it. Remember, in programmable content, a file is a mere component of a bigger picture - few files ever being guaranteed to be self-contained.

A flip-side to this method of achieving `structural integrity` however is that if a file is *mis-named*, rather than *mis-placed*, there isn't much you can do in order to determine whether the file has in fact been mis-placed or whether it has been mis-named.

```bash
# Does this file belong under spiderman, or has it been mis-named?
$ /projects/hulk/shots/1000/spiderman_1000_v001_marcus.ma
```

Structural integrity is important and should be sought after, but perhaps there is a better way. Duplicating information in this manner is a closer to a work-around than a solution.

Consider the following hierarchy:

```bash
$ /projects/hulk/shots/1000/marcus/v001.ma
```

The full path of `v001.ma` is shorter, yet retains the same amount of information as in the previous example.

This is the Programmable Content method of managing data.

### Database for metadata

### Schema

```bash
$ /projects/<project>/shots/<shot>/private/<user>/<software>
```

This isn't necessarily pre-defined anymore.