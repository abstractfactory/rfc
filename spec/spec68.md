# Bi-directionality in relationship tracking

Pros and cons of bi-directionality in maintaining integrity of relationships between objects.

* Name: http://rfc.abstractfactory.io/spec/68
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

* nodes either point towards another node, their reverse relationship thus being implied via context. 
* disadvantage of this is, in a large network, it may take some time for this implied data to get computer.
* disadvantage of keeping a link alive on both ends is their potential to mis-fire and otherwise get out of sync.