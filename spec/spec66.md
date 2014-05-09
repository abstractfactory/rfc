# Push/Pull Node

Definition of a node capable of recieving input from multiple sources of data.

* Name: http://rfc.abstractfactory.io/spec/66
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

Let's start with some definition; a `node` represents a location in a data-store, such as a file-system. This may be a folder or a file, an object within third-party software such as a Maya DAG object.

The `node` isn't interested in what this location may actually look like, but encapsulates what they all have in common; relatives.

```python
# Typical hierarchy
        _____
       |     |
       |_____|
      ____|____
   __|__     __|__
  |     |   |     |
  |_____|   |_____|

```

The `node` is then built upon by other, data-store agnostic objects, such as the `item` which wraps `node` in graphics for display in lists/trees.

# The problem

A naive approach to this problem may be to subclass `node` for each use.

![](https://dl.dropbox.com/s/g0v5a67nzktop74/first-version.png)

Which, at first, may seem perfect. In our case, there was one source of information, the file-system and only one use for it - [Dash][dash]. We later required access to metadata, and rather than strapping this onto each individual application I chose to integrate it with `node` in the form of a `data` attribute. The attribute, when called, would make use of the second input, `openmetadata`.

![](https://dl.dropbox.com/s/kzxavx53kny8b5p/second-version.png)

There are now three variations of `node`. One for just disk-access, one for both disk-access and metadata-access and finally one for just metadata-access. Later, it became necessary to extend upon this model to also include support for representing information in arbitrary data-stores; e.g. Autodesk Maya.

![](https://dl.dropbox.com/s/m8v2mzkkkbtysy3/third-version.png)

The number of variations escalated exponentially. However at this point, this wasn't clear to me. Instead, I favoured certain combinations over others, which is reasonable as some of these would rarely, if ever, be required. There was however a gap in this logic and in the level of scalability possible with this model.

![](https://dl.dropbox.com/s/jl8vmsny7b912jo/fourth-version.png)

Maintanability at this point was not particularly pleasant, not to mention the hassle of introducing another type, as it would have be required to conform to the overall interface and data compatibility of its sibling objects.

# A solution

With [git][], you can `fork` a `repository` and `pull` from it. This makes your `fork` independent of its original and may be modified in isolation. Once the changes you've made are satisfactory, you can `push` those changes back onto the original.

This is sometimes referred to as a **Push/Pull** workflow. Let's have a look at how such a workflow applies to our scenario.

![](https://dl.dropbox.com/s/v5pe5lbv298mfd4/pushpull.png)

Here, a single `node` can pull from multiple sources. A `node` can choose to pull from a single source, two, or all source at once. The key thing to note here is the combination of which  inputs are allowed to be used, making this model infinitely extensible to support any arbitrary input.

Once a modification has been completed, the information may then be passed to a `push` which may persistently record the modification onto the original data-store.

# Decentralised

A side-effect of the benefit listed above is the notion of decentralisation. Like with [git][], modifications are performed separate from the source information. This provides two main benefits:

* Pushes may be deferred
* Changes may remain non-persistent

### A deferred push

By not applying changes immediately, we've opened up the doors for significant scalability benefits; both real-time and off-line.

### Real-time scalability

In the vast majority of cases, a user navigating a user-interface isn't interested in what is actually happening within a data-store. Instead, a user is interested in communicating his intentions to the computer as quickly and efficiently as possible. The computer can then take additional time to complete these requests.

Ultimately, it matters not how many modifications is being requested by the user, graphical interfaces relying on a `node` can never become bogged down in under-the-hood details.

### Off-line scalability

Qt relies on events. Events are triggered from many places at tight intervals and some of these events cancel each other out - such as when a widget is requested to be painted red, but before it has a chance to get painted, it is requested to be painter blue.

This form of `deduplication` is applicable to us as well. Ultimately, performance, but also stability, is increased. As the back-end responsible for storing these changes will encounter less work.

### A temporary change

When changes aren't applied directly, we've opened up the potential for temporariy modifying a `node` to fit our immediate, but perhaps temporary, purpose.

For example, a `node` may contain subdirectories, some of which are discarded via the "no folders starting with a dot"-filter. The subdirectories could be removed from the contained children, knowing without altering the physical equivalent on disk.

# Architecture

Each `source` provides a `target`. A `node` must then support the given `target` before it can accept data from the given `source`.

![](https://dl.dropbox.com/s/2xmy0t49mr20kbd/target.png)

Here, `node` is being fed information from `disk` and `om` sources.

```python
>>> pull(node)
>>> node.data['somedata'] = 5
>>> push(node)
```

# Compatability

Due to the only requirement of each `source` is to provide a `target`, a `source` may ultimately see use outside of its original use-cases. For example, [Open Metadata][om] is another node-based data management system. It deals with children and data, just like the `node` presented here.

[om]: http://abstractfactory.io/om
[git]: http://git-scm.com/
[dash]: https://github.com/abstractfactory/dash