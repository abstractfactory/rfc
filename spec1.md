# INP - Inheritance Pattern

This document further defines inheritance within the Abstract Factory RFC.

* Name: https://github.com/abstract-factory/rfc/spec:1 (1/INH)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: none
* Inherited by: *

Copyright (c) 2014 the Editor and Contributors.

This Specification is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This Specification is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses>.

# Change Process

This document is governed by the [Consensus-Oriented Specification System (COSS)][].

# Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119][].

# Goal

Inheritance is a mechanism often employed in Object-Oriented programming practices to promote code reuse.

In the Abstract Factory RFC, inheritance plays a similar role and lay grounds for a hierarchy in which children may infer content via its parent.

# Architecture

Specifications provide a `inherits` and an optional `inherited by` property specifying from where to inherit content.

# Example

* Name: https://github.com/abstract-factory/rfc/spec:3 (3/MVP)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:2
* Inherited by: spec:3, 

Here, [spec:3][] inherits from [spec:2][] meaning [spec:3][] includes content specified by [spec:2][] - including copyright notice, change process and language - on a header-by-header notice.

Furthermore, an inherited specification provides the interface for which to design descendant specifications.

[Consensus-Oriented Specification System (COSS)]: http://www.digistan.org/spec:1/COSS
[RFC 2119]: http://tools.ietf.org/html/rfc2119
[Divide and Conquer]: http://en.wikipedia.org/wiki/Divide_and_conquer_algorithm
