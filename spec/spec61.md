# Terminal Open Metadata

Definition of `om` the terminal version of Open Metadata

* Name: http://rfc.abstractfactory.io/spec/61
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

To provide terminal access to the fundamental properties of Open Metadata.

# Architecture

```bash
# Syntax
[command] [key] {value}
```

```bash
# Example
$ om name Marcus
$ om name
Marcus
$ om /address/street Blackwall Way
$ om /address/street
Blackwall Way
$ om /address
street=Blackwall Way
```