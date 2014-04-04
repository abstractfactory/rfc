# Storage Agnostic Metadata (SAM)

This document describes a method of making Open Metadata agnostic to where data is ultimately stored; be it on disk, in a database or an in-memory data-structure.

* Name: https://github.com/abstract-factory/rfc/spec:12 (12/AOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:1

Copyright, Change Process and Language is derived via inheritance as per [spec:1][]

# Goal

Open Metadata was originally designed as an agnostic method of traversing metadata in a hierarchical fashion. The initial implementation utilised the familiarity of the file-system, but the use of Open Metadata extends beyond management of files and folders.

Therefore, we'll break apart the general mechanisms with those interacting with a file-system into a separate `service`

Each `service` featuring interaction mechanisms with a target data-storage mechanism.

# Architecture

We'll introduce `service` to the Open Metadata object-model. A `service` is based on SOA, or Service-Oriented Architecture, and essentially means a (potentially) remote object providing "services", in this case read/write functions, within a given domain, such as a file-system or other database such as SQL.