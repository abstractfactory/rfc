# Open Metadata Temporal Resolution

This document defines a method of minimising writing operation in an attempt to optimise situations where writing happens quickly one after another.

* Name: http://rfc.abstractfactory.io/spec/46
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC10

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

> This document assumes prior knowledge of Open Metadata and RFC10.

When running `om.write()` or `om.dump()` many times consequtively - e.g. 10.000 times within one second - it may not be desireable to maintain history of each edit. Nor may it be interesting to even bother writing the 9.999 initial values as the last value will ultimately be the one that lasts beyond one second.

# Architecture

Introduce a queing mechanism which queues dump tasks and only performs contained tasks once a certain amount of time has passed - e.g. 1 second.

At every second, the queue is flushed and values within are dumped to disk.