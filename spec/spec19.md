# Storage Agnostic Metadata

This document describes a method of making Open Metadata agnostic to where data is ultimately stored; be it on disk, in a database or an in-memory data-structure.

* Name: http://rfc.abstractfactory.io/spec/19
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: raw

Copyright, Change Process and Language can be found in RFC1

# Goal

Open Metadata was originally designed as an agnostic method of traversing metadata in a hierarchical fashion. The initial implementation utilised the familiarity of the file-system, but the use of Open Metadata extends beyond management of files and folders.

Therefore, we'll break apart the general mechanisms with those interacting with a file-system into a separate `service`

Each `service` featuring interaction mechanisms with a target data-storage mechanism.

# Architecture

We'll introduce `service` to the Open Metadata object-model. A `service` is based on SOA, or Service-Oriented Architecture, and essentially means a (potentially) remote object providing "services", in this case read/write functions, within a given domain, such as a file-system or other database such as SQL.