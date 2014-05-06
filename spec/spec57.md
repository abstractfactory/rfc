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
$ dash hulk/1000
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
* `strap`

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

At each turn `dash` performs a breath-first search in a hierarchy of content, starting from the current working directory (`CWD`) and stopping at the first item found. 

```bash
Breadth-first search of hierarchy.
Each level is recursively searched until a match is found.

Given the hierarchies:

|CWD                         |CWD
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
level 0 |                      |  CWD  |                
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

# CWD successfully set to CWD/hulk/shots/1020
```

Alternatively, a command may be daisy-chained for aggregated searches such as the one above, using the forward-slash operator.

```bash
$ dash machine/1000
$ maya
```

`maya` then is a `bootstrapper` around the actual executable, first performing a workspace query; creating a workspace if none is found, based on the active username.

### Strap

A "bootstrapper" modifies environment variables in preparation for running software. As defined in Further Reading below, there are two primary methods of preparing context; DIRECT and DEFERRED.

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
# This is effectively what a bootstrapper is doing:
$ set PYTHONPATH=/projects/hulk/scripts
$ set PATH=/projects/hulk/executables
$ maya
```

See also [Bootstrapping Software][bootstrapping]

As executables on their own cannot be expected to make use of the context provided by `dash`, a bootstrapper must be present to prepare or otherwise educate software about the context under which it is to be run.

Bootstrappers MUST be created using `strap`

```bash
$ strap maya
```

Here, `maya` is an existing executable accessible via the terminal. `strap` then "bootstraps" this executable into an additional executable and puts it onto the path, in front of all other executables so as to ensure that the bootstrapped versions is called in place of the original.

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

Thus bootstrappers take precedence over the executables they strap.

### Strap and context

Bootstrappers are stored within the current context.

```bash
$ dash hulk
$ strap maya
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
$ strap maya
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
$ strap maya maya-2014x64
```

# Further reading

The following are some of the things that may come to change the above; alternatives or additions that may break the overall model. At the end of this section you will have gained a greater perspective on the benefits and disadvantages associated with terminal context sensitivity.

### Contextual Metadata

Provide access to contextual metadata.

```bash
$ dash hulk/1000
$ dash $SHOT
1000
$ dash $PROJECT
hulk
$ dash $METADATA
SHOT=1000
PROJECT=hulk
```

#### Key definition

Where do the keys `SHOT` and `PROJECT` come from?

A `key` MUST be pre-defined and there MAY be three (3) methods of defining them.

#### 1. Built-in

Here, each `key` is coded into `dash`. `dash` MAY provide a plugin-based architecture into which end-users could implement custom keys.

* External configuration

Here, keys are recorded into a external configuration of sorts, for example a `.json` serialised dictionary:

```json
{
    "PROJECT": "$ROOT/projects/{0}",
    "SHOT": "$PROJECT/shots/{0}"
}
```

In this dictionary, each key represents a `dash` `key`; their values represent an expression used in resolving the given `key` into a `dash` `value`; `ROOT` being hard-coded into `dash` and configurable as specified in #Absolute Context below.

* Self-describing content

Here, each directory provides their own key(s).

```bash
$ cd /project/hulk/shots/1000
$ dash $PROJECT
```

Here, `dash` traverses upwards through the hierarchy, querying each folder for their `key` and attempts to match it with `$PROJECT`

```bash
$ /projects/hulk/shots/1000 <-- "do you have a key called 'PROJECT'?" -- no
$ /projects/hulk/shots <-- "do you have a key called 'PROJECT'?" -- no
$ /projects/hulk <-- "do you have a key called 'PROJECT'?" -- yes
hulk
```

See also [Open Metadata][om]

### When to alter the environment

Context can either be applied upon running `dash` or upon running a `bootstrap`. I will refer to these as `DIRECT` and `DEFERRED` respectively.

```bash
# DIRECT
$ dash hulk/1000

# Here, varaibles have been exported into the environment
# to reflect the current context of PROJECT=hulk and SHOT=1000
$ echo $PROJECT
hulk

# DEFERRED
$ dash hulk/1000
$ echo $PROJECT
<nothing>

# Here, metadata such as $PROJECT haven't been exported into
# the environment. `dash` may compensate for this:
$ dash $PROJECT
hulk
```

#### DEFERRED

In a DEFERRED approach, context is applicable only to commands that support it, e.g. `bootstrap` versions of executables.

```bash
$ dash hulk/1000
$ maya
# Environment is being modified..
# Executable is being launched..
```

It is the `bootstrap` responsibility to read from the current context and apply it in an application-specific manner. For instance, based on the shot, certain scripts may become available, or certain dependencies resolved.

#### DIRECT

Conversely, variables are exported upon running the command using a DIRECT approach.

```bash
$ dash hulk/1000
# Environment is being modified..
$ maya
# Executable is being launched..
```

Which allows for use of other commands that isn't necessarily designed to read from the context provided by `dash`.

```bash
$ customApp
# Error: Command not found
$ dash hulk/1000
# Environment is being modified..
# - export PATH=/custom/bin:PATH
$ customApp
# Running customApp..
```

Here, the directory of `customApp` is being added to the PATH environment variable, making this command available when previously it was not. This could potentially be used to provide context sensitive commands, so as to not dilute the global namespace with every possible command; thus utilising a benefit of context sensitivity.

### Alternative environment

This RFC is based on providing context sensitivity by exporting variables to the active environment. There are a few limitations to this approach.

1. Child-processes have difficulty altering any aspect of its parent-process.
2. Altering persistent environment variables does not take effect on other running terminals, until said terminals have been restarted and thus picked up the new environment.
3. Environment variables support strings only; thus no support for bool, numbers or arbitrary data.

#### Sidecar files

An alternative to storing variables in the native environment provided by each running process on Posix- and Nt-based platforms may be to use sidecar files.

In short, a sidecar file is a standalone file on disk that may substitute storing metadata in the environment to storing it in this file. The sidecar file would be accessible globally, similar to environment variables, but with two (2) main differences:

1. Any process may alter it.
2. Processes does not require a restart upon an altered sidecar file.
3. Sidecar files may store arbitrary data.

Thus eliminating all limitations of native environment variables.

See also: [Methods of storing metadata][RFC24]
See also: [Open Metadata][om]

#### Sidecar files and concurrent access

A disadvantage of favouring sidecar files to environment variables lies in their direct inability to provide a per-session environment.

```bash
# Terminal A
$ dash hulk/1000
```

```bash
# Terminal B
$ dash spiderman/1000
```

```bash
# Terminal A
$ maya
# Launching maya under context: spiderman/1000..
```

### Deep hierarchies and breadth-first search

In cases where a context does not exist and a hierarchy is deep, say 1000 levels deep, 100 children at each level, the breadth-first query may take a substantial amount of time to complete.

```bash
$ dash notexist/500
# Error: notexist not found
```

I see two potential solutions to this problem; inclusion and exclusion.

#### Inclusion

At each level of a hierarchy, a folder may specify inclusion into the breadth-first search.

```bash
$ cd /projects/hulk/etc
$ touch include
```

Prior to searching any directory, `dash` first consults each directory for an existing `include` flag and if one exists, only included directories are searched further.

#### Exclusion

Once inclusion has been completed, each directory is searched; except those that are excluded.

```bash
$ cd /projects/hulk/catpictures
$ touch exclude
```

### Absolute context

`dash` is relative to your `CWD`. The `CWD` is said to be the `root` of `dash`.

```bash
# This starts by looking for `hulk` at your `CWD`
$ dash hulk
```

However, it isn't uncommon for a terminal to launch with the `CWD` set to a user's home directory and in a collaborative environment, projects are unlikely to reside there.

Thus `dash` MUST provide the ability to override `root` into an arbitrary absolute path.

```bash
# Either in the current session
$ dash --root
/home/marcus
$ dash --root /projects
$ dash --root
/projects
```

Or persistently, somehow..

[bootstrapping]: http://rfc.abstractfactory.io/spec/62
[RFC24]: http://rfc.abstractfactory.io/spec/24
[om]: https://github.com/abstractfactory/openmetadata
[adapter]: http://en.wikipedia.org/wiki/Adapter_pattern