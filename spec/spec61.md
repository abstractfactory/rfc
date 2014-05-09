# Open Metadata-cli

Definition of the command-line interface of Open Metadata.

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
$ [command] [key] [value] [option]
```

```bash
# Example
$ om name Marcus
$ om name
Marcus
$ om /address/street "Blackwall Way"
$ om /address/street
Blackwall Way
$ om /address
street=Blackwall Way
```

### The `@` operator

Cast, or force, a certain datatype.

```bash
$ om myflag @Flag
$ om mytext "a string" @Text
$ om myfloat 5 @Float
$ om mylike True @Like
```