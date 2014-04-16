# Hierarchical Representation

This document describes the requirements for elements in a tree (nodes).

* Name: http://rfc.abstractfactory.io/spec/37
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC38
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

To represent a `node` within a hierarchy and to provide for manipulation of said `node`.

A `node` MUST support:

* `REQ01`: Representation of children
* `REQ02`: Representation of parent(s)
* `REQ03`: Addition of children (virtual)
* `REQ04`: Subtraction of children (filtering)
* `REQ05`: Forwarding/re-direction
* `REQ06`: In-memory metadata (private)
* `REQ07`: External metadata (public)

# Architecture

```python
# Terminology
* `node`
```

A `node` MUST provide an interface for displaying contents of direct descendants and MUST provide reference to its parent.

### Representation of children

```python
# Terminology
* `leaf-node`
* `leaf-item`
```

For the sake of argument, picture a folder on disk. A folder may contain multiple files and/or folders. A file however may not.

Thus a folder has n-number of children whereas a file has 0; yet both are nodes within a hierarchy - a file referred to as being a `leaf-node`.

In a graphical user interface, an `item` within a list represents a `node`. An `item` MAY or MAY NOT contain children and if not is considered a `leaf-item`.

A pattern emerges.

```python
# Two types of nodes
    ___________        __________ 
   |           |      |          |
   |   child   |------|   leaf   |
   |___________|      |__________|
 
```

```python
# Terminology
* A file is a leaf node, not the other way around.
```

This is important; a leaf represents the end of a branch. An empty group would also be referred to as a leaf node.

### Representation of parent(s)

The plurality is important. It implies that a given `node` may possess multiple parents. Again, picture a folder on disk. Normally, one folder has one parent, but a folder one MAY make a `junction` from one folder to another. This means a folder appears in two locations simultaneously and thus will have two (potentially) separate parents.

```python
parent1
    childA
parent2
    childA
```

And thus, a `node` must provide for multiple parents. In situations where folders appear in multiple locations, the original folder is referred to as `original` and will be the first-returned parent upon query.

```python
parent1
    childA  <-- original
parent2
    childA  <-- second
```

### Addition of children

In a graphical user interface it may be necessary to provide for items that aren't naturally present within a physical hierarchy.

#### Scenario A

Again, picture a folder on disk. Within a graphical list of items, each child within this folder is represented by a box.

```python
 __________
|          |
|  child1  |
|__________|
|          |
|  child2  |
|__________|
|          |
|  child3  |
|__________| 

```

From a usability point-of-view, it may become necessary to append a "Add" box to this layout.

```python
 __________
|          |
|  child1  |
|__________|
|          |
|  child2  |
|__________|
|          |
|  child3  |
|__________| 
|          |
|   add    | <--- added "virtual" item
|__________|

```

At this point, we represent a hierarchy that is not longer true to the original vision of the parent `node` at the gain of convenience to the user.

#### Scenario B

Consider situations in which you require a merge of multiple hierarchies into one;

```python
 ______________________________
| assets                       |  # Assets stored on central-harddrive-A
|     plane                    |
|     pilot                    |
|______________________________|
                +
 ______________________________
| assets                       |  # Assets stored on remote-harddrive-B
|     diver                    |
|______________________________|
                +
 ______________________________
| assets                       |  # Assets available locally
|     my_asset                 |
|______________________________|
                =
 ______________________________
| assets                       |  # Resulting hierarchy
|     plane                    |
|     pilot                    |
|     diver                    |
|     my_asset                 |
|______________________________|

```

### Subtraction of children

```python
# Terminology
* `filter`
```

Filtering is an important part of information management. Filtering may impose a constraint on the number of nodes displayed, nodes displayed by a certain criteria (e.g. name, depth, size) or flags (e.g. hidden, invisible) or an arbitrary rule (e.g. only first parent, do not follow symlinks).

### Forwarding

Forwarding is the act of passing control over to another `node`. Consider a node without any data but instead references another `node`.

```python
parent1
  child  <-- junction..

parent2  <-- ..to here
  subchild1
  subchild2

# Resulting hierarchy
parent1
  child
    subchild1
    subchild2
```

# Metadata

```python
# Terminology
* `metadata`
* `private`
* `public`
```

In addition to support for parent(s) and children, a `node` MUST support the notion of `metadata`.

`metadata` is divided into two categories; `private` and `public`. `public` `metadata` lives external to the object (e.g. such as on disk, within a database) wheras `private` `metadata` resides within.

`public` `metadata` is powered by Open Metadata and MUST be provided with access to:

* Reading
* Adding
* Removing
* Modifying

`private` `metadata` is powered by whatever features the programming languages supports; including, but not limited to, strings, ints, bools, floats.