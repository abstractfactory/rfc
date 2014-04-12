# Pipeline Processing of Hierarchical Representations

An extension to RFC37 in regards to the addition and subtraction of children.

* Name: http://rfc.abstractfactory.io/spec/38
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

In RFC16 we specified the requirements of a `node`. This document will define a potential implementation of `REQ03`, `REQ04` and `REQ05`.

* `REQ03`: Addition of children (virtual)
* `REQ04`: Subtraction of children (filtering)
* `REQ05`: Forwarding/re-direction

Pipeline is defined on Wikipedia as:

>  a set of data processing elements connected in series, where the output of one element is the input of the next one. - http://en.wikipedia.org/wiki/Pipeline_(computing)

We will apply the same pattern to each `child` of a `node`.

# Architecture

```python
# Keywords
* `node`
* `process`
 __________       ___________       __________ 
|          |     |           |     |          |
|   node   |---->|  process  |---->|   node   |
|__________|     |___________|     |__________|
 
```

### Virtual children

`REQ03` represents a method of appending children to an existing hierarchy of children.

```python
 __________       ___________ 
|          |     |           |
|  parent  |---->|   child   |
|__________| .   |___________|
             .
             .   . . . . . . .
             .   .           .
             . . .   child   .  <-- virtual child
                 . . . . . . .

```

#### Implementation A

The simplest approach would be to explicitly append a child to a given `node`

```python
class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self._children = list()
        self._vchildren = list()

        if parent:
            parent._children.append(self)

    @property
    def children(self):
        for vchild in self._vchildren:
            yield vchild

        for child in self._children:
            yield child


>>> node = Node('test')
>>> child = Node('child', parent=node)
>>> vchild = Node('vchild')
>>> node._vchildren.append(vchild)

>>> gen = node.children
>>> print gen.next().name
'vchild'
>>> print gen.next().name
'child'
```

#### Implementation B

This may be reproduced using pipeline processing as such:

```python
class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.processes = list()
        self._children = list()
        self._vchildren = list()

        if parent:
            parent._children.append(self)

    @property
    def children(self):
        for process in self.processes:
            self = process(self)

        if self:
            while self._vchildren:
                yield self._vchildren.pop()

            for child in self._children:
                yield child

def add_vchild(node):
    vchild = Node('vchild')
    node._vchildren.append(vchild)
    return node

# Test
parent = Node('parent')
child = Node('child', parent)

parent.processes.append(add_vchild)
print parent.children
[Node('child'), Node('vchild')]

```

### Filtering

`REQ04` represents a method of filtering the output of a given node via some form of criteria.

```python
 ___________      ___________      ___________ 
|           |    |           |    |           |
|   alpha   |    |   beta    |    |   gamma   |  <-- input
|___________|    |___________|    |___________|
      |________________|________________|
                  _____|_____ 
                 |           |
                 |   filter  |  <-- criteria; input != gamma
                 |___________|
       ________________|
 _____|_____      _____|_____
|           |    |           |
|   alpha   |    |   beta    |  <-- output
|___________|    |___________|
 
```

Here, `gamma` is stripped from the output by the filtering-process due to the criteria "input != gamma".

#### Implementation

```python
class Node(object):
    def __init__(self, name, parent=None):
        """Store each process alongside each child"""
        self.name = name
        self.processes = list()
        self._children = list()

        if parent:
            parent._children.append(self)

    @property
    def children(self):
        """
        Each child is run through each available process.
        The process can either output the node as-is, or not
        at all. If the child remains at completion of each process
        it is yielded; otherwise it is not.

        """

        for child in self._children:
            for process in self.processes:
                if not child:
                    break
                child = process(child)
            
            if not child:
                continue

            yield child

def input_not_gamma(node):
    """Example filter"""
    if node.name != 'gamma':
        return node
    return None

# Test
parent = Node('parent')
alpha = Node('alpha', parent)
beta = Node('beta', parent)
gamma = Node('gamma', parent)

parent.processes.append(input_not_gamma)
print parent.children
[Node('alpha'), Node('beta')]
```