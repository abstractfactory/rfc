# Persistent Software References

This document descibes a method of storing persistent references to software on disk.

* Name: http://rfc.abstractfactory.io/spec/29
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC21
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

In RFC21 we spoke of discovering software on a local workstation.

```From the book Game Engine Architecture by Jason Gregory, 2009```

### Text configuration files

By far the most common method of saving and loading configuration options is by placing them into one or more text files. The format of these files varies widely from engine to engine, but it is usually very simple. For example, Windows INI files (which are used by the Ogre3D renderer) consist of flat lists of key-value pairs grouped into logical sections.

```ini
[SomeSection]
Key1=Value1
Key2=Value2
[AnotherSection]
Key3=Value3
Key4=Value4
Key5=Value5
```

The XML format is another common choice for configurable game options files.

### Compressed binary files.

Most modern consoles have hard disk drives in them, but older consoles could not aff ord this luxury. As a result, all game consoles since the Super Nintendo Entertainment System (SNES) have come equipped with proprietary removable memory cards that permit both reading and writing of data. Game options are sometimes stored on these cards, along with saved games. Compressed binary files are the format of choice on a memory card, because the storage space available on these cards is oft en very limited. 

### The Windows registry

The Microsoft Windows operating system provides a global options database known as the registry. It is stored as a tree, where the interior nodes (known as registry keys) act like fi le folders, and the leaf nodes store the individual options as key-value pairs. Any application, game or otherwise, can reserve an entire subtree (i.e., a registry key) for its exclusive use, and then store any set of options within it. The Windows registry acts like a carefully-organized collection of INI fi les, and in fact it was introduced into Windows as a replacement for the ever-growing network of INI fi les used by both the operating system and Windows applications.

### Command line options

The command line can be scanned for option settings. The engine might provide a mechanism for controlling any option in the game via the command line, or it might expose only a small subset of the game’s options here.

### Environment variables

On personal computers running Windows, Linux, or MacOS, environment variables are sometimes used to store confi guration options as well.

### Online user profiles

With the advent of online gaming communities like Xbox Live , each user can create a profi le and use it to save achievements, purchased and unlockable game features, game options, and other information. The data is stored on a central server and can be accessed by the player wherever an Internet connection is available.