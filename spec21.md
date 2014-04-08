# Software Discovery

This document describes methods of discovering software on a local operating system.

* Name: http://rfc.abstractfactory.io/spec/21
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC29
* Tags: software discovery, dealing with change

Copyright, Change Process and Language can be found in RFC1

# Goal

Software discovery is the process of finding software by way of relative reference.

```python
# Absolute reference
c:\program files\adobe\photoshop\ps.exe

# Relative reference
photoshop
```

Discovering software via relative reference is useful in scenarios where it is important to de-couple the software you write from the software you interact with.

For example, an application launcher, as defined in Wikipedia is:

> ..a computer program that helps a user to locate and start other computer programs.

In this situation, absolute references might look something like this.

```python
c:\program files\maya\maya.exe
c:\program files\adobe\photoshop\ps.exe
c:\program files\foundry\nuke\nuke.exe
```

Which suffers from two immediate problems.

* `PROBLEM1`: It isn't portable to other platforms 
* `PROBLEM2`: It forces users on a valid platform to position software in a location determined by the software

A more portable alternative is the use of relative references:

```python
maya
photoshop
nuke
```

Now the application launcher is independent of the underlying platform and where software is ultimately located. The application launcher and references to software have been de-coupled from its platform.

The issue then is, how do we resolve a relative reference into an absolute reference on the target platform?

# Architecture

```python
  __________         ___________         __________
 |          |       |           |       |          |
 | relative |------>| resolve() |------>| absolute |
 |__________|       |___________|       |__________|
 

```

The process of resolving a relative reference into an absolute reference may vary based on requirements and preference. Let's have a look at some of the more common ways in which this is dealt with.

### No resolve

Simplest approach. Not resolving paths involves assumptions and guesswork.

```python
# Fingers crossed that everyone is running Windows, and
# everyone has their software installed exactly here:
c:\program files\maya\maya.exe
c:\program files\adobe\photoshop\ps.exe
c:\program files\foundry\nuke\nuke.exe
```

### Path generation

The act of compiling a full path via templates.

```python
# Python example
>>> reference = 'gimp'

>>> windows_template = r'c:\Program Files\{software}\{software}.exe'
>>> linux_template = r'/opt/{software}/{software}'

>>> resolved_windows = windows_template.format(software=reference)
c:\Program Files\gimp\gimp.exe

>>> resolved_linux = template_linux.format(software=reference)
/opt/gimp/gimp
```

Path-generation solves `PROBLEM1`. We can get around `PROBLEM2` by ensuring consistent installations on all involved workstation within a facility; which is generally considered common-practice anyway.

But what about situations where you are working with more than your own facility? What about situations in which you require outsourcing to other facilities or freelancers?

Registration may be better suited for this.

### Registration

The act of making binaries discoverable by name.

```
# Command-line example
:> set PATH=PATH;c:\Program Files\Gimp
:> gimp
```

Our references have not changed; but their method of resolving into absolute paths has. By making executables discoverable by name at the OS-level we can ensure discoverability across environments where the initial installations of software are out of our hands.

There is however a caveat; the process of registration is still required at each workstation.
