# Shopfront Repository Pattern

This pattern defines `private` versus `public` repositories and their differences.

* Name: http://rfc.abstractfactory.io/spec/9
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Tags: versioning
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

When working towards a goal, it can sometimes be difficult to distinguish between what is presentable and what is work-in-progress; resulting in inconsistency in the manner in which results are ultimately presented to others.

#### Synonyms

`private` is sometimes also referred to as

* `development`
* `work in progress`
* `source`

`public` is sometimes also referred to as

* `published`
* `production`

# Architecture

When creating content, there are exactly two types of results; `private` and `public` 

* `private`: work-in-progress or in-development style results not relevant to others but merely a preamble to `public` results.
* `public`: results conformed to a set of standards so as to provide a consistent service for others.

In a sense, private results reside at the back of a craftsman's shop; rough, unpolished and nonsensical to the untrained eye. Public results however fully encapsulates its value and worth in a form easily digestible to others; so as to attract as many as possible.