# dependent

definition of dependent, a software dependency resolver

* Name: http://rfc.abstractfactory.io/spec/30
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

- to provide for dependency resolution when establishing a tool-chain.

See also [Package Management System on Wikipedia][pms]
See also [Rez](https://github.com/nerdvegas/rez)

# Architecture

`dependent`

```bash
$ dependent pip-0.3
pip-0.3.26
setuptools-0.6.44
python-2.6.1
```

# Rez

An evaluation of Rez.

### A Environment Management System (EMS)

Though explicitly stated as not being a EMS along with providing a definition of EMS, it does alter a running environment to provide for context sensitivity, similar to how EMS has been defined.

See also [EMS Definition][definition]

### A Package Configuration System (PCS)

Rez provides a syntax and tools for resolving required dependencies along with the cascading dependencies of dependencies.

### Compilation Build-system

Though not 

* rez only supports posix
* rez assumes version-controlled software, e.g. mercurial/subversion

[pms]: http://en.wikipedia.org/wiki/Package_management_system
[definition]: https://github.com/nerdvegas/rez/wiki#what-is-rez-not
