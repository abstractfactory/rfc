# Representations Pattern

This document describes a method facilitating the need for multiple data-types co-existing within any given version.

* Name: http://rfc.abstractfactory.io/spec/7
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC1, RFC2, RFC3, RFC4, RFC6
* Tags: versioning, publishing
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Language

In addition to the language defined in RFC1, DOCUMENT refers to any digital content, including but not limited to files and folders.

# Goal

In situations where DOCUMENT is strongly coupled to the software in which it was created, it may be beneficial to maintain multiple sets of DOCUMENT per version so as to facilitate its use in software other than the one in which the DOCUMENT was originally created. Each set of DOCUMENT may be referred to as a `representation` of a particular `version`.

* Versioning is further defined in RFC33.

# Architecture

Given the DOCUMENT `mydoc`, one or more instances of `representation` may be provided:

```python
mydoc
|-- version 1
	|-- mydoc.txt
	|-- mydoc.doc
	|-- mydoc.rtf
	|-- mydoc.md
```

Where each suffix represents use in target software:

* `txt` 	-- Originating from Notepad
* `doc` 	-- Originating from Microsoft Office
* `rtf` 	-- Originating from Microsoft Wordpad
* `md`		-- Originating from Markdown

At this point, a single DOCUMENT is accessible from within multiple sets of software.

Another example taken from the film industry, `myanimation` was initially created in Autodesk Maya 2015.

```python
myanimation
|-- version 1
	|-- myanimation.mb-2014
	|-- myanimation.mb-2013
	|-- myanimation.fbx
	|-- myanimation.abc
	|-- myanimation.obj
		|-- frame 1.obj
		|-- frame 2.obj
		|-- ...
	|-- myanimation.mov
```

Here, a single DOCUMENT created in a newer version of Maya is accessible from previous versions of the same software, in addition to software supporting the various standards `fbx`, `abc` and `obj`, as well as a format accessible by video players, potentially representing the version to non-technical personell.
