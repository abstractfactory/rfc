# Zero Metadata (ZMO)

This document describes an extension of Open Metadata for high-concurrency and/or high-performance scenarios using the ZeroMQ networking library.

![](https://dl.dropbox.com/s/ghnv20fy1u725az/spec13_zom_v001.png)

* Name: https://github.com/abstract-factory/rfc/spec:11 (11/MCE)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Inherits: RFC1

Copyright, Change Process and Language is derived via inheritance as per [RFC1][].

# Goal

In high-concurrency situations file-writing runs the risk of being written to simultaneously from multiple sources. This document then describes a few ways in which this may be dealt with while still retaining the flexibility and generality of Open Metadata itself.

ZMO MUST remain compatible with both RFC10 (Open Metadata) and RFC11 (OOM).