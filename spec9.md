# SHP - Shopfront Repository Pattern

This pattern defines `private` versus `public` repositories and their differences.

* Name: https://github.com/abstract-factory/rfc/spec:4 (4/TVP)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:3

Copyright, Change Process and Language is derived via inheritance as per [spec:1][]

# Goal

When working towards a goal, it can sometimes be difficult to distinguish between what is presentable and what is work-in-progress; resulting in inconsistency in the manner in which results are ultimately presented to others.

# Architecture

When creating content, there are generally speaking two sets of results; `private` and `public` 

* `private`: work-in-progress or in-development style results not relevant to others but merely a preamble to `public` results.
* `public`: results conformed to a set of standards so as to provide a consistent service for others.

In a sense, private results reside at the back of a craftsman's shop; rough, unpolished and nonsensical to the untrained eye. Public results however fully encapsulates its value and worth in a form easily digestible to others; so as to attract as many as possible.