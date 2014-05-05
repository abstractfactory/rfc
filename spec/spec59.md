# Omlang, pure programmable content

The Open Metadata programming language.

* Name: http://rfc.abstractfactory.io/spec/59
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

In traditional programming, variable definitions and their values are stored together with their business logic. Conversely, Omlang separates storage from usage.

```python
# Variables and values are stored on disk
content
|-- red
|-- green
|-- blue
```

```python
# The variables are then used in Omlang as follows:
 color = red + green + blue
```

# Use

* Create content
* Evaluate content
* Search content

### Create

Using Omlang to create new content

```python
rgb = r + g + b
# Where `r`, `g` and `b` are previously
# existing content on disk. `rgb` is written
# once the code compiles/runs.
```

### Evaluate

Using Omlang to evaluate expressions.

```python
# The expression:
/full/path/$WORKSPACE/version$NUMBER*2

# Resolves into, e.g.
/full/path/marcus/maya/version12
```

### Search

Using Omlang as a search-language, similar to SQL.

# Architecture

Omlang consists of two orthogonal types:

* `variable`
* `command`

```python
 color = red + green + blue
|_____| |__________________|
command      variables
```

Where a `command` is the equivalent of a Python property; directly assignable but with programmable response/action. A `command` is not persistent and does therefore not exist on disk. A `variable` however exists on disk and is accessible with `omlang` by name.

### Nested variables

Variables in Omlang are hierarchical; meaning they may be nested within other variables. Accessing nested variables follows the same conventions a accessing individual nested members within a file-system.

```python
# Variables and values
content
|-- description
    |-- weight
    |-- height
```

Which is then used like this:

```python
# Logic
bmi = description/weight / (description/height ** 2)
```

### Current working directory & breadth-first search

Omlang revolves around the current working directory. Variables not directly available from the current working directory is searched, depth-first, through the contained hierarchy.

```bash
# Hierarchy
cwd
|-- red
|-- green
|-- parent
    |-- blue
```

```bash
# omlang
color = red + green + blue
```

Here, `blue` isn't found directly within `cwd` and is resolved into using `parent/blue` instead.