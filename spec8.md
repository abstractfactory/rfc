# Keywords and cross-referencing

Keywords and cross-referencing is an optimisation extension of the Abstract Factory RFC that allows for specifications to reference parts of other specifications as a means of clarification and information reuse.

* Name: https://github.com/abstract-factory/rfc/spec:8 (8/KCR)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:1

Copyright, Change Process and Language is derived via inheritance as per [spec:1][].

# Goals

To alleviate the need for repetition in specifications, specifications allow for use of `keywords` and `cross-referencing` as a means of encapsulating meaning and re-using existing information within another specification.

# Architecture

* `keywords`: short, memorable identifiers surrounded in back-ticks (`)
* `cross-referencing`: keyword with embedded @ indicates a reference to included keyword.

# Example

This description references `@another-keyword`

Via referencing, one can distill new information more quickly and avoid repetition.