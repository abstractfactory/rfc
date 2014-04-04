# IVP - Immutable Versioning Pattern

This document describes an approach to versioning adopted from the Software Development industry that I call Immutable Versioning Pattern (IVP) and is a polylithic approach as opposed to a monolithic approach such as the one proposed by RFC3/MVP.

* Name: https://github.com/abstract-factory/rfc/spec:2 (2/IVP)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>

Copyright (c) 2014 the Editor and Contributors.

This Specification is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This Specification is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses>.

# Change Process

This document is governed by the [Consensus-Oriented Specification System (COSS)][].

# Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119][].

# Goals

The opposite of versioned is monolithic and may thus be referred to as polylithic. In a monolithic process, there are no record of events or change and all that exists at any given point in time is here and now.

The monolithic approach has a few problems; mainly that it discourages change as change would imply a new permanent state.

In a versioned process, change is "layered"; meaning that no change affects previous state. This encourages change as it completely eliminates the cost of making mistakes.

# Definition

* Refering to past, present and future states MUST be explicit.

# Reference Implementation

Versioning may take the form of increasing numerical suffixes to files and folders in the form of:

`name:separator:version`

Where `name` is a short identifier for the product in development, `separator` being a unique character visually separating head from tail and `version` an increasing integer; higher numbers meaning later versions.

`myAsset_v1`

It can sometimes be helpful to maintain a fixed-length on the number of integers in versioning so as to simplify parsing.

>>> product = 'myAsset_v001'  # A Python string
>>> version = int(product[:-3])

Always assuring that the last n number of characters represents the version makes it possible to perform simple string-manipulation techniques to derive a version from any given product.

[Consensus-Oriented Specification System (COSS)]: http://www.digistan.org/spec:1/COSS
[RFC 2119]: http://tools.ietf.org/html/rfc2119
[versioning]: http://en.wikipedia.org/wiki/Software_versioning