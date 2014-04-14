# Monolithic Versioning Pattern

This document describes a method of tracking change with a single document.

* Name: http://rfc.abstractfactory.io/spec/3
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Tags: versioning, publishing
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Language

In addition to the language defined in RFC1, DOCUMENT refers to any digital content, including but not limited to files and folders.

# Goal

The goal of Monolithic Versioning is to maximise concurrency whilst minimising the amount of manual intervention required in keeping a hierarchy of tasks up to date at the cost of an implicit system with the potential to cause unwanted side-effects.

# Architecture

Monolithic Versioning, also known as Mutable Versioning, is the act of saving DOCUMENT whilst (optionally) maintaining history somewhere external to said DOCUMENT. Examples include systems such as [Git][], [Subversion][] and [Perforce][].

As opposed to [Polylithic Versioning][] (RFC2), changes are `implicit` and require no intervention on the part of the user when it comes to performing an `update`.

# Git

# Subversion

# Perforce

[Git]:http://git-scm.com/
[Subversion]: http://subversion.apache.org/
[Perforce]: http://www.perforce.com/
[Polylithic Versioning]: http://rfc.abstractfactory.io/spec/2
[Consensus-Oriented Specification System (COSS)]: http://www.digistan.org/spec:1/COSS
[RFC 2119]: http://tools.ietf.org/html/rfc2119n