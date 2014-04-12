# Keywords and cross-referencing

Keywords and cross-referencing is an optimisation extension of the Abstract Factory RFC that allows for specifications to reference parts of other specifications as a means of clarification and information reuse.

* Name: http://rfc.abstractfactory.io/spec/8 (8/KCR)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Tags: general
* State: retired

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

To alleviate the need for repetition in specifications, specifications allow for use of `keywords` and `cross-referencing` as a means of encapsulating meaning and re-using existing information within another specification.

# Architecture

* `keywords`: short, memorable identifiers surrounded in back-ticks (`)
* `cross-referencing`: keyword with embedded @ indicates a reference to included keyword.

# Example

This description references `@another-keyword`

Via referencing, one can distill new information more quickly and avoid repetition.