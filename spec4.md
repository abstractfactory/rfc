# TVP - Timed Versioning Pattern

Timed Versioning Pattern attempts to compromise between the benefits of both IVP and MVP to allow for automatic updates, without loosing the ability to later refer back to specific states in development.

* Name: http://rfc.abstractfactory.io/spec/4 (4/TVP)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:3

Copyright, Change Process and Language is derived via inheritance as per [spec:1][]

# Goals

TVP implements an implicit system of version control which allows for referencing past states via the use of time-stamps.

The problems imposed by IVP is the manual intervention involved in updates. MVP fixes this, but removes our ability to refer to arbitrary points in history.

As a compromise, TVP stores history exactly like IVP but allows artists to instead refer to an additional single monolithic version that is constantly kept at the highest, or recommended, version.

# Definition

* Transitioning between versions MUST NOT require manual intervention.
* Referring to past, present and future states MUST be explicit.

# Architecture

Versions may be classified as being either `historical` or `current`. Furthermore, states may be classified as being either `latest` or `recommended` and `historical` versions MUST include a `timestamp`

* `historical`: persistent and immutable, just like IVP, and MUST include a `timestamp`
* `current`: a singleton and the one referred to by others and is continually replaced to reflect either `latest` or `recommended` states.
* `latest`: last state at which a product was saved.
* `recommended`: human-decided factors govern whether or not a version is recommended or not (usually those backwards-compatible with previous versions or those representing the next evolutionary step (e.g. an upgrade))
* `timestamp`: a unique point in time with precision appropriate for the given application. (suggested year:month:day:hour:minute for long-running projects and month:day:hour:minute:second for shorter ones)

# Reference Implementation

The `current` version MUST be allowed to take any form and `historical` versions MUST include a `timestamp`

* `name`
* `name:separator:timestamp`

Where `name`, like in IVP, is a short human-readable identifier and `timestamp` a unique identifier for the time at which the product was made.

* `/product/myAsset`
* `/product/history/myAsset_1403251846`

Products referencing `myAsset` MUST include a `timestamp` at which the reference took place.

* `/otherproduct/myProject`
