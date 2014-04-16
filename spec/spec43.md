# Simple Task Distribution Pattern

* Name: http://rfc.abstractfactory.io/spec/43
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Tags: distribution
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

Distribute task(s) to worker(s). To utilise the total sum of available resources whilst ensuring a minimal loss of resources.

Ground rules:

* GRU01: Client may independently assert required resources
* GRU02: Worker may independently assert available resources
* GRU03: Worker may process multiple requests simultaneously