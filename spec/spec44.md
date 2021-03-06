# The Event Pattern

This document defines a pattern of propagating signals through hierarchies of components.

* Name: http://rfc.abstractfactory.io/spec/44
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Tags: publishing
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal


### Event Propagation

An event generated by a child MUST propagate to its parent; and so on so forth until there are no more parents left.

### Multiple observers

One significant difference between `Signal` and `Request` is that `Request` supports multiple inputs. Multiple observers may contribute to the return value of a given request; the first one to return an appropriate response wins.

In the majority of cases, a request will have 0-1 observers.