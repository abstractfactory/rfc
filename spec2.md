# IVP - Immutable Versioning for Production

This document describes the traditional approach to versioning most commonly adopted by Visual Effects production houses around the world as of today (March, 2014) that I call Immutable Versioning for Production (IVP)

* Name: https://github.com/abstract-factory/rfc/spec:1 (1/IVP)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>

Copyright (c) 2014 the Editor and Contributors.

This Specification is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This Specification is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses>.

# Change Process

This document is governed by the [Consensus-Oriented Specification System (COSS)][].

Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119][].

Goals

IVP is meant to facilitate an iterative development-style which is in direct contrast to the [Waterfall-model][] which is still very much alive but not recommended in Visual Effects production because of assumptions implied by it, such as:

1. Change is considered rare
2. Information flows in only one direction
3. The direction of a project doesn't change

The primary goal of COSS is to facilitate the process of writing, proving, and improving new technical specifications. A "technical specification" defines a protocol, a process, an API, a use of language, a methodology, or any other aspect of a technical environment that can usefully be documented for the purposes of technical or social interoperability.

COSS is intended to above all be economical and rapid, so that it is useful to small teams with little time to spend on more formal processes.

Principles:

We aim for rough consensus and running code.
Specifications are small pieces, made by small teams.
Specifications should have a clearly responsible editor.
The process should be visible, objective, and accessible to anyone.
The process should clearly separate experiments from solutions.
The process should allow deprecation of old specifications.
Specifications should take minutes to explain, hours to design, days to write, weeks to prove, months to become mature, and years to replace.

Specifications have no special status except that accorded by the community.

Architecture

COSS is designed around fast, easy to use communications tools. Primarily, COSS uses a wiki model for editing and publishing specifications texts.

The domain is the conservancy for a set of specifications in a certain area.
Each domain is implemented as an Internet domain, hosting a wiki and optionally other communications tools.
Each specification is a set of wiki pages, together with comments, attached files, and other resources.
Important specifications may also exist as subdomains, i.e. child wikis.
Individuals can become members of the domain by completing the necessary legal clearance. The copyright, patent, and trademark policies of the domain must be clarified in an Intellectual Property policy that applies to the domain.

Specifications exist as multiple pages, one page per version of the specification (see "Branching and Merging", below), which may be assigned URIs that include an incremental number. Thus, we refer to a specification by specifying its domain, number, and short name. New versions of the same specification will have new numbers. The syntax for a specification reference is:

<domain>/spec:<number>/<shortname>
For example, this specification is www.digistan.org/spec:1/COSS. The short form 1/COSS may be used when referring to the specification from other specifications in the same domain.

Every specification (including branches) carries a different number. Lower numbers indicate more mature specifications, higher numbers indicate more experimental specifications.

COSS Lifecycle

Every specification has an independent lifecycle that documents clearly its current status.

A specification has six possible states that reflect its maturity and contractual weight: