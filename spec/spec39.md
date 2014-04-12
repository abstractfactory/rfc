# Pipi Data Access Object

This document describes DAOs and their relevance in Pipi

* Name: http://rfc.abstractfactory.io/spec/39
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: raw
* Related: RFC23, RFC24, RFC25, RFC27

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

Abstract underlying details of data acquisition and manipulation so as to provide for an object with a straightforward interface capable of being used in situations requiring traversal and data access.

# Architecture

Data in Pipi is database-agnostic; meaning that data may reside on a file-system, in a relational database, in-memory or within any arbitrary storage model.

In Pipi, there are three layers of abstraction for any given database to make this possible.

* The Node
* The Data Access Object
* The Service

### The Node

A `node` represents an element within a tree or graph and encapsulates functionality for manipulating said element.

### The Data Access Object

The `DAO` wraps a given `service`, providing a CRUD interface with which a `node` may interact with a given system.

CRUD is:

* Create
* Read
* Update
* Delete

### The Service

Services represents required functionality at a level closest to a given system and encapsulates it within a flat hierarchy of functions.

```python
import os

def ls(path):
	return os.listdir(path)
 
```

The `DAO` then uses functions related to its CRUD operation in order to provide a consistent interface for `node` objects regardless of the underlying system.

Here is similar functionality as above, but for Autodesk Maya:

```python
from maya import cmds

def ls(path):
	return cmds.listRelatives(path)
```