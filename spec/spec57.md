# Textual Software Configuration

Define the most efficient method of configuring software via text.

* Name: http://rfc.abstractfactory.io/spec/57
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC21, RFC29
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

Software configuration is the act of running software with zero or more of the following:

* arguments
* keyword arguments
* custom environment

Textual Software Configuration defines three (3) commands for performing software configuration based on context via a command line/terminal.

* `dash`
* `-`
* `wrap`

### Target group

`dash` et. al. is designed for every-day use by artists. As such, the requirements are that `dash` MUST be:

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

Here are some examples of non-compliant syntaxes.

```bash
# Too specific
$ dash /projects/hulk/shots/1000

# Too many flags
$ dash --project hulk/1000 --app maya --version 2014 --arch x64

# Esoteric characters (*from bcore)
$ dash @/projects/a ---packages.python.version=2.6 launch
```

References

* [bcore](https://github.com/Byron/bcore/issues/19)

### Extended use

`dash` MUST comply with `REQ01` and `REQ02`, but MAY offer additional support for complex setup; e.g. when using `dash` with automated or scripted utilities.

Extended features

* Version specificity
* 

# Architecture

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
[command] [query] [flag]
```

At each turn `dash` performs a breath-first search in a hierarchy of content, returning the first item found. Alternatively, a commands may be daisy-chained for aggregated searches such as the one above.

```bash
$ dash machine/1000
$ maya
```

`-` then is a shorthand for `dash`

```bash
$ - machine/1000
$ maya
```

`maya` then is a wrapper around the actual executable, first performing a workspace query; creating a workspace if none is found, based on the active username.

### Wrap

As executables on their own are unaware of context considerations, a wrapper must be present to prepare or otherwise educate software about the context under which it is to be run.

Wrappers MUST be created using `wrap`

```bash
$ wrap maya
```

Here, `maya` is an existing executable accessible via the terminal. `wrap` then "wraps" this executable into an additional executable and puts it onto the path, in front of all other executables so as to ensure that the wrapped versions is called in place of the original.

```bash
# Before
PATH=/original/path

# After
PATH=/wrapped/path:/original/path
```

Where the hierarchy of executable may look like this:

```bash
original
|-- maya
|-- xsi
|-- nuke

wrappers
|-- maya
|-- xsi
|-- nuke
```

Thus wrappers take precedence over the executables they wrap.

### Wrap and context

Wrappers are stored within the current context.

```bash
$ dash hulk
$ wrap maya
```

Here, the wrapped equivalent of `maya` isn't visible outside of the `hulk` context.

```bash
# Running a non-wrapped executable
$ dash starwars
$ maya
```

Globally accessible wrappers are stored at the root of `dash`

```bash
# This wrapped equivalent of `maya` is accessible from any child within root.
$ dash --clear
$ wrap maya
```

### Specificity

A user may be as specific as is required. In an empty environment with only one project, it may not be necessary to specify a job.

```bash
$ - 1000
$ maya
```

However in a vast environment with hundreds of projects, shots and sequences, it may not be enough to specify only job and shot.

```bash
$ - lotr/seq/102b/1000
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

# A custom name is given to the wrapped equivalent
$ wrap maya maya-2014x64
```