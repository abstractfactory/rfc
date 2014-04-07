# Local Software Discovery

This document describes methods of software discovery within a local operating system.

* Name: http://rfc.abstractfactory.io/spec/21 (21/LSD)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC22
* Tags: software discovery, dealing with change

Copyright, Change Process and Language can be found in [RFC1][]

# Goal

How do you program towards executables of software when you can guarantee neither availability nor platform?

# Architecture

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

Given a `criteria`, the `launcher` presents avaiable `software` via a set of `references`.

For our discussion, our criteria is `Pulp` - a digital asset used in a fictional game that I just made up. `Pulp` is made using the latest version of `Software X` and a rather old but trusty version of `Software Y`, these are our references.

As `launcher` will run on multiple computers, on multiple platforms in multiple locations at various times, we can't be sure of where `Software X` is located; whether it is located locally on the file-system, or maybe it's a web-application running off the cloud and drawn in your browser. Either way, our `launcher` can't make any assumptions about it.

For the sake of discussion, our criteria will come from disk and will have been put there by humans.

```python
+-- project
|   +-- game
|   |   +-- Pulp
```

The next step is to store references in a way that makes them accessible via `Pulp`. One way is to store them in a text document somewhere.

```python
# my_references.txt
/project/game/pulp
    Software X
    Software Y
```

We can trim this file by storing it directly within `Pulp`

```python
# references.txt
Software X
Software Y
```

### Method 2 - Generating paths


### Method 3 - Meeting half-way
