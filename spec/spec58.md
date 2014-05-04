# Kom - A communications library

A lightweight inter-process communications library.

* Name: http://rfc.abstractfactory.io/spec/58
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

In a Service-Oriented Architecture, services are distributed across an arbitrary amount of workers. Each service may then be utilised outside of and beyond the context under which it was originally designed; facilitating de-coupled components and a large amount of code re-use.

Kom is a communications library designed to distribute software in the same manner; where software may make use of other software as though they were native and local. Call it, Software-Oriented Architecture.

As software is a collection of services, a Software-Oriented Architecture is then a higher-level construct than a Service-Oriented Architecture, useful in scenarious where the larger whole consists of many smaller applications; such as a Digital Asset Management System.