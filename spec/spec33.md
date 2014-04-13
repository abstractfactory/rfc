# Versioning

This document describes the purpose of versioning and version control software.

* Name: http://rfc.abstractfactory.io/spec/33
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Tags: versioning
* Related: RFC2, RFC3, RFC4
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Language

In addition to the language defined in RFC1, DOCUMENT refers to any digital content, including but not limited to files and folders.

# Goal

Versioning serves exactly two purposes; tracking change and maintaining referential integrity.

#### Related

* [Monolithic Versioning Pattern][]
* [Polylithic Versioning Pattern][]
* [Temporal Versioning Pattern][]

### Maintaining Referential Integrity

```python
 _____________
|             |
|  document1  |
|_____________|
       |
 ______|______
|             |
|  document2  |
|_____________|
       |
 ______|______
|             |
|  document3  |
|_____________|

```

Here, `document2` references/depends on `document1`; i.e. if `document1` changes, so does `document2`. A `graph` such as this may grow indefinitely and with it the difficulty in assuring that the `link` inbetween each DOCUMENT remains valid; this is called **maintaining referential integrity**.

### Tracking Change

```python
                _____________
               |             |
       ________|  document1  |_______ 
      |        |_____________|       |
      |               |              |
 _____|______   ______|______   _____|______
|            | |             | |            |
|   state1   | |   state2    | |   state3   |
|____________| |_____________| |____________|
                      |
                ______|______
               |             |
               |  document3  |
               |_____________|

```

Each change to DOCUMENT may be referred to as a `state` of said DOCUMENT. Here, `document1` provides one or more instances of `state`, each produced at various stages of development, however `document3` only references `state2`. A `state` is the main mechanism with which to **track change**.

# Architecture

Exactly two (2) versioning patterns exist followed by variations of each; `Monolithic` and `Polylithic`. In `Monolithic` versioning, DOCUMENT is continuously overwritten and changes to any given DOCUMENT may be optionally tracked external to said DOCUMENT; this may be referred to as `implicit tracking`.

The [Monolithic Versioning Pattern][] is further defined in RFC3

In `Polylithic` versioning, each change to DOCUMENT is made explicit,  requiring references to each DOCUMENT to be manually maintained; this may be referred to as `explicit tracking`.

The [Polylithic Versioning Pattern][] is further defined in RFC2

### Implicit Tracking

In implicit tracking, a DOCUMENT is unaware of changes to referenced DOCUMENT; the change is said to be implicit and the `update` process said to be automatic or implied.

### Explicit Tracking

In explicit tracking, a DOCUMENT maintains reference to a fixed `state` and any `update` handled manually; either via user intervention or external mechanisms, such as Version Control Software (VCS).

# Version Control Software

Maintaining referential integrity and tracking change is a major undertaking and yet vital to any project involving more than a single worker. That is why there are companies out there focusing solely on providing the best approach to the variety of scenarios requiring versioning.

Examples of Version Control Software providing a `Monolithic` method of versioning include [Git][], [Subversion][] and [Perforce][]. `Polylithic` version control software however is far less common and is mainly developed ad-hoc in productions that require them.

[Git]:http://git-scm.com/
[Subversion]: http://subversion.apache.org/
[Perforce]: http://www.perforce.com/
[Monolithic Versioning Pattern]: http://rfc.abstractfactory.io/spec/3
[Polylithic Versioning Pattern]: http://rfc.abstractfactory.io/spec/2
[Temporal Versioning Pattern]: http://rfc.abstractfactory.io/spec/4
