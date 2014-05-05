# Terminal Navigation

Definition of `goto` A command-line utility for effectively navigating large hierarchies of content.

* Name: http://rfc.abstractfactory.io/spec/60
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC57
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

This document defines one (1) command-line utility for effectively navigating large hierarchies of content.

* `goto`

Syntax MUST align with RFC57.

# Architecture

`goto` provides two (2) methods of use; `breadth-first` and `aliased`.

### Breadth-first

```bash
# Go to shot 1000 of hulk, breadth-first
$ goto hulk/1000
# cwd sucessfully set to /projects/hulk/shots/1000
```

The `breadth-first` method of `goto` performs a breadth-first search of content, starting from the current working directory (`cwd`) and stopping at the first match.

Thus, given the hierarchy:

```
cwd
|-- machine
|   |-- shots
|       |-- 1000
|       |-- 2000
|       |-- 3000
|-- hulk
|-- starwars
|-- spiderman
```

```bash
$ goto machine
# ..would return cwd/machine

# Whereas
$ goto 1000
# ..would *possibly* return cwd/machine/shots/1000
# if no other match is found at an earlier `level`
# in any of the ther potential hierarchies; `hulk`,
# `starwars` or `spiderman`.

# And..
$ goto machine
$ goto 1000
# ..would be guaranteed to return cwd/machine/shots/1000

# ..which may be shortened to
$ goto machine/1000
```

### Aliased

Users may jump to pre-defined locations with `aliases` (not to be confused with [bash `alias`][alias], although their functions are identical)

```bash
# Go to private dir of current context, alias
$ cd /some/dir
$ goto --home
# cwd successfully set to /projects/hulk/shots/1000/private/marcus
```

Aliases are prefixed with a double-dash which hides the possibility of using flags with `goto`.

Aliases are defined by passing a value to the alias.

```bash
$ goto --myalias /projects/hulk/my_custom_folder
# alias successfully defined
```

And override existing aliases

```bash
$ goto --home /not/my/home
# alias successfully defined
```

### Custom aliases and keywords

Aliases may resolve keywords

```bash
$ goto --myalias $PROJECT/my_custom_folder
# alias successfully defined
```

Where `$PROJECT` represents an environment variable.

```bash
$ echo $PROJECT
# /projects/hulk
```

### Persistence

Like [bash `alias`][alias], `goto` aliases does not persist across sessions, but must instead be re-defined each time.

A possible solution then is to have your shell re-define these upon launch.

[alias]: http://tldp.org/LDP/abs/html/aliases.html