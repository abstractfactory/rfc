# Local Software Discovery

This document describes methods of software discovery within a local operating system.

* Name: http://rfc.abstractfactory.io/spec/21 (21/LSD)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC22
* Tags: software discovery, dealing with change

Copyright (c) 2014 the Editor and Contributors.

This Specification is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This Specification is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses>.

# Change Process

This document is governed by the [Consensus-Oriented Specification System (COSS)](http://www.digistan.org/spec:1/COSS).

# Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

# Goal

When developing software to run other software, i.e. a `launcher`, the launcher must somehow be told of available software so that it may present them to you and ultimately run the software you specify.

This could easily be achieved by simply storing an absolute path to each available software within the program-code and have it list those. However, availability changes with time and place. Software you have installed locally today may not exist on other system and may indeed not exist on *your* system not too far from now; either due to becoming deprecated (i.e. you don't need them anymore) or to being replaced (e.g. by a next version perhaps).

The issue escalates once you head over to an unfamiliar system. A system whose software you did not install. Perhaps a system that you would not know how to even start looking for installed software (think Windows versus Linux).

Rather than storing absolute paths to executable within our program, wouldn't it be better to store platform-agnostic references to software? References that may be resolved into absolute path in an fashion suitable to wherever our software is running?

This document will attempt to document a few methods of achieving this, each with their respective pros and cons.

Legend

* `system` -- refers to operating system.

# Architecture

Let's define some keywords.

* `launcher`
* `criteria`
* `reference`
* `software`

```python
  __________ 
 |          |
 | criteria |
 |__________|
      |
      |
  ____v_____         ___________         __________
 |          |       |           |       |          |
 | launcher |------>| reference |------>| software |
 |__________|       |___________|       |__________|

```

Our `launcher` is given a set of `criteria` which is resolved into an absolute path to `software` via a given `reference`.

For our discussion, our criteria is `Pulp` - a digital asset used in a fictional game that I just made up. `Pulp` is made using the latest version of `Software X` and a rather old but trusty version of `Software Y`, these are our references.


### Method 1 - The hard way

The brute-force approach to this problem is to simply go look for the software within a system and hard-code the path to its executable. This works fine in many cases, especially if you're only concerned about your own system, but once you head into using the same `launcher` in a different environment

### Method 2 - Generating paths


### Method 3 - Meeting half-way

