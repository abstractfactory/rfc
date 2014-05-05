# Terminal Context Sensitivity

Definition of context sensitivity as provided via a terminal.

* Name: http://rfc.abstractfactory.io/spec/57
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC60
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

To provide a user with context sensitivity within a terminal.

Context sensitivity means to alter a running session of a terminal in such a way that any further action to take effect only within the given context.

### Example - Save

Without context sensitivity, a command must include specificity:

```bash
# Save shot `1000` of project `hulk`
$ save --project hulk --shot 1000
```

With context sensitivity, the same command may be abbreviated:

```bash
# Specify context prior to running command.
$ dash hulk/1000
$ save
```

### Use-case

Why context sensitivity?

**Run pre-determined software**

Particular versions of software may be inferred via context.

```bash
# Without context sensitivity
$ maya-2014x64

# With context sensitivity
$ dash hulk
$ maya
```

Here, a particular version of Maya has been inferred by `hulk` rather than explicitly stated. This could be used as a means of unifying software versions across particular contexts; such as projects.

**Performing multiple commands within a given context**

Sometimes, a user may perform a prolonged amount of work towards a similar context. Thus context could potentially be used as means of reducing line- and word-count as well as ensuring that each operation adheres to an identical context.

```bash
# Without context sensitivity
$ export --project hulk --shot 1000
$ archive --project hulk --shot 1000
$ close --project hulk --shot 1000

# With context sensitivity
$ dash hulk
$ export
$ archive
$ close
```

**Wrapping commands with a similar interface**

Sometimes, the commands used towards a given context may stem from a variety of authors or may have been developed at different times, at different locations and for different requirements.

Thus context provides a means of bridging such commands so as to reduce the number of signatures any user must remember.

See also [Adapter Pattern][adapter]

```bash
# Without context sensitivity
$ export -proj hulk --sht 1000
$ archive -ctx hulk:1000
$ close @gtd:/hulk/1000

# With context sensitivity
$ dash hulk/1000
$ export
$ archive
$ close
```

Thus, with context sensitivity, *commands* may be kept minimal and implicit.

### Target audience

`dash` is aimed at non-technical personnel; e.g. artists. As such, the requirements are that `dash` MUST be:

* `REQ01` Easy to remember
* `REQ02` Quick to write

Examples of an ideal syntax

```bash
# Run maya, from hulk project
$ dash hulk
$ maya

# Run maya, from a specific shot
$ dash hulk/1000
$ maya
```

Examples of a non-ideal syntax.

```bash
# Too specific
$ dash /projects/hulk/shots/1000

# Too many flags
$ dash --project hulk/1000 --app maya --version 2014 --arch x64

# Esoteric characters (*from bcore)
# - @, triple-dash and dot
$ dash @/projects/a ---packages.python.version=2.6

# Multiple operations (*from bcore)
# - Both setting, and running software from the same command
$ dash hulk/1000 launch
```

References

* [bcore](https://github.com/Byron/bcore/issues/19)

### Extended use

This specification MUST comply with `REQ01` and `REQ02` but MAY offer additional support for complex use; targeted at using `dash` by automated or scripted means.

**Absolute versioning**

Override pre-determined software versions.

```bash
$ dash hulk/1000 --/packages/maya/version 2013
```

**Exclusion**

Exclude pre-determined software using the `--not` flag.

```bash
$ dash hulk/1000 --not /plugins/maya/matrixNodes
```

# Architecture

Terminal Context Sensitiviy defines two (2) commands for performing software configuration based on context via a command line/terminal.

* `dash`
* `bootstrap`

Context is determined by zero (0) or more of the following:

#### 1. Arguments

Software-specific flags without value

```bash
# Example
$ maya -hideConsole
```

#### 2. Keyword arguments

Software-specific flags with value

```bash
# Example
$ maya -proj /home/marcus
```

#### 3. Custom environment

Modified environment based on context.

```bash
# Example
# Enter into the `hulk` context
$ set PYTHONPATH=/projects/hulk/scripts
$ set PATH=/projects/hulk/executables

# Run Maya 2013x64 as defined by the `hulk` context
$ maya
```

### Syntax

Given the hierarchy:

```
jobs
|-- machine
|   |-- shots
|       |-- 1000
|       |-- 2000
|       |-- 3000
|-- hulk
|-- starwars
|-- spiderman
```

A user may select `machine`, `1000` and finally run `maya` with the following set of commands.

```bash
$ dash machine
$ dash 1000
$ maya
```

```bash
# The syntax of `dash` is as follows:
[command] [query] {flag}
```

At each turn `dash` performs a breath-first search in a hierarchy of content, starting from the current working directory (`cwd`) and stopping at the first item found. 

```bash
Breadth-first search of hierarchy.
Each level is recursively searched until a match is found.

Given the hierarchies:

|cwd                         |cwd
|-- lotr                     |-- hulk
|   |-- shots        and     |   |-- shots
|       |-- 1000             |       |-- 1020
|       |-- 2000             |       |-- 2310
|       |-- 3000             |       |-- 2540
|       |-- 4000             |       |-- 3300

Run the command
$ dash 1020

        |                       _______                 
        |                      |       |                
level 0 |                      |  cwd  |                
        |                      |_______|                
--------|                     _____|_____               
        |                ____|___    ____|___           
        |               |\ \ \ \ |  |        |           
level 1 |               | \lotr \|  |  hulk  |
        |               |\_\_\_\_|  |________|           
--------|          _________|___________|______________ 
        |      ___|____    ____|___    ____|___    ____|___ 
        |     |        |  |\ \ \ \ |  |\ \ \ \ |  |\ \ \ \ |
level 2 |     |  1020  |  | \2310 \|  | \2540 \|  | \3300 \|
        |     |________|  |\_\_\_\_|  |\_\_\_\_|  |\_\_\_\_|


* Dashed boxes are not selected.

# CWD successfully set to cwd/hulk/shots/1020
```

Alternatively, a command may be daisy-chained for aggregated searches such as the one above, using the forward-slash operator.

```bash
$ dash machine/1000
$ maya
```

`maya` then is a `bootstrapper` around the actual executable, first performing a workspace query; creating a workspace if none is found, based on the active username.

### Bootstrap

A "bootstrapper" modifies environment variables in preparation for running software. The purpose is to provide an illusion of "context sensitivity" to the user; allowing them to use terminology such as "I'm running `SoftwareX` from `ProjectY`"

```bash
# Non-bootstrapped executable
$ maya
```

The above runs Maya, similar to how it would normally be run after a fresh install on a fresh OS.

```bash
# Bootstrapped executable
$ maya
```

Different executable, same function. The bootstrapped `maya` effectively hides the original executable so as to make transparent the act of performing environment modifications prior to executing the specified software.

```bash
# Under-the-hood example; environment is modified prior to running `maya`
$ set PYTHONPATH=/projects/hulk/scripts
$ set PATH=/projects/hulk/executables 
$ maya
```

As executables on their own are unaware of context considerations, a bootstrapper must be present to prepare or otherwise educate software about the context under which it is to be run.

Bootstrappers MUST be created using `bootstrap`

```bash
$ bootstrap maya
```

Here, `maya` is an existing executable accessible via the terminal. `bootstrap` then "bootstraps" this executable into an additional executable and puts it onto the path, in front of all other executables so as to ensure that the bootstrapped versions is called in place of the original.

```bash
# Before
PATH=/original/path

# After
PATH=/bootstrapped/path:/original/path
```

Where the hierarchy of executable may look like this:

```bash
original
|-- maya
|-- xsi
|-- nuke

bootstrappers
|-- maya
|-- xsi
|-- nuke
```

Thus bootstrappers take precedence over the executables they bootstrap.

### Bootstrap and context

Bootstrappers are stored within the current context.

```bash
$ dash hulk
$ bootstrap maya
```

Here, the bootstrapped equivalent of `maya` isn't visible outside of the `hulk` context.

```bash
# Running a non-bootstrapped executable
$ dash starwars
$ maya
```

Globally accessible bootstrappers are stored at the root of `dash`

```bash
# This bootstrapped equivalent of `maya` is accessible from any child within root.
$ dash --clear
$ bootstrap maya
```

### Specificity

A user may be as specific as is required. In an empty environment with only one project, it may not be necessary to specify a job.

```bash
$ dash 1000
$ maya
```

However in a vast environment with hundreds of projects, shots and sequences, it may not be enough to specify only job and shot.

```bash
$ dash lotr/seq/102b/1000
$ maya
```

As each `part` of the given query.

### Clashing

A breadth-first search includes the possibility of clashing names. Consider the following hierarchy.

```bash
jobs
    machine
        shots
            1000
            2000
            3000
    hulk
        shots
            1000
            2000
            3000
```

A user specifying an inadequate level of specificity may end up selecting the wrong context.

```bash
$ dash 1000
$ maya
# Did the user select shot 1000 of `machine` or `hulk`?
```

### Feedback

```bash
$ dash 1000

No existing workspace found for user `marcus`
- Create? [Yes]/No:

```

### Flags

```bash
# Run graphical user interface of dash, rooted at machine/1000
$ dash machine/1000 --show

# Do not confirm with user about a non-existing workspace
$ dash machine/1000 --autocreate

# The current context is cleared.
$ dash --clear

# A custom name is given to the bootstrapped equivalent
$ bootstrap maya maya-2014x64
```

[adapter]: http://en.wikipedia.org/wiki/Adapter_pattern