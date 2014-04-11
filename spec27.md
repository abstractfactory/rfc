# Pipi Architecture

This document dives into explaining the higher-level architecture as well as some of the decisions involved in finding it.

![](../images/27/title.png)

* Name: http://rfc.abstractfactory.io/spec/27
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: raw

Copyright, Change Process and Language can be found in RFC1

# Goal

To make the Pipi code base as easily digestable and extendable as possible for an agile development-style. This is in contrast to the previous architecture in which all code reside within a single root directory and extensions scattered within.

# Architecture

To facilitate the requirements specified in RFC25, Pipi is divided into 4 modules*

* Custom Development
* Binding
* Domain
* Foundation

Foundation defines objects that operate across all other modules and represents the lowest-level implementations of re-usable components.

Domain defines objects that only operate within a single domain, or industry - `film`, `games`, `tv` or `web` to name a few. Each Domain features objects only relevant to the specific Domain - `film` may for instance define `shot` and `sequence` objects, whereas `games` have their own `level` and `player` objects.

Bindings are application-specific implentations also known as Integrations. E.g. `pimaya` is a Domain-module featuring objects only relevant to Autodesk Maya; such as `reference` or `offline file` objects.

Finally, the Custom Development module represents the work put on top of Pipi at each facility using it and could potentially contain the glue code that connects the overall operation of the studio with Pipi.

\* Module in this context is defined as

> Each of a set of standardized parts or independent units that can be used to construct a more complex structure. - Google Definition

This modularisation facilitates two main purposes;

1. The ability to learn, use and evaluate Pipi one module at a time.
2. The extension and/or modification of each module in isolation.

# Service-Oriented Architecture (SOA)

Pipi evolves around a Service-Oriented Architecture, which is defined as:

> Service-oriented architecture (SOA) is an architectural style for building
systems based on interactions of loosely coupled, coarse-grained, and
autonomous components called services. Each service exposes processes and
behavior through contracts, which are composed of messages at discoverable
addresses called endpoints. A service's behavior is governed by policies that are
external to the service itself. The contracts and messages are used by external
components called service consumers. - SOA Patterns, Arnon Rotem-Gal-Oz, 1.2

Which makes each components distributable, decentralised pieces of intelligence.

To facilitate for SOA, Pipi employs the concept of a `service` which is defined as

> a facility supplying some public demand - Merriam-Webster's dictionary

Which is further defined as

> A service should provide a distinct business function, and it should be a coarse-grained piece of logic. Additionally, a service should implement all of the functionality promised by the contracts it exposes. One of the characteristics of services is service autonomy, which means the service should be mainly self-sufficient. - SOA Patterns, Arnon Rotem-Gal-Oz, 1.2.1
