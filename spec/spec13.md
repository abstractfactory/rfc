# Zero Open Metadata

This document describes an extension of Open Metadata for high-concurrency and/or high-performance scenarios utilising the ZeroMQ networking library.

![](../images/13/title.png)

* Name: http://rfc.abstractfactory.io/spec/13
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC10

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

> "If I write to file A, and you write to file A, who wins?"

Your operating system is very adapt at distributing the tasks you assign to it. However there are times when even the smartest operating system with the smartest of hard-drives can corrupt your data; it is after all, the real world.

One possible source of this corruption is multiple writes to a single location. Since Open Metadata is all about collaborative edits, how can it ensure that data is never written from one location while at the same time being written from another?

# Architecture

Lets have a look at some of the ways of dealing with this problem in ascending order of complexity.

### Introspection

Possibly the most straight-forward solution is to ask a file-system which files are currently in use and never try and write to one that is, but instead wait for it to become free. (lsof on linux, openfiles.exe on windows)

### Lock-files

Similar to Introspection, another (brute-force) approach of assuring that there is only ever one writer at a time is to use lock-files.

```python
+-- folder
|   +-- .meta
|   |   +-- data.string
|   |   +-- data.string.lock
```

A lock-file is merely an empty file somehow designating which files are "locked" for edits. When a lock-file exists, no other than the creator of the lock-file may edit the locked file.

Only upon completing the edit does the creator then remove his lock-file and thus restore permission for others to create lock-files of their own in preparation for their edits.

#### Lock-files and deadlocks

There is of course the possibility of an edit not completing successfully and thus leaving behind its lock-file. In these cases, the locked files are forever locked and can never be edited; not even to remove the lock-file.

In cases such as these it may be necessary to introduce a time-slot within which each edit is expected to take place. During edit, the editor could receive a heartbeat every so often - say 20 ms - to which the editor is required to respond. Upon failure to respond, the lock-file is automatically removed and the editor then looses permission to further write to this destination without re-establishing a lock-file.

### Broker

One possibly solution is to introduce a `broker`.

![](../images/13/broker.png)

It would then be up to the `broker` to delegate or queue requests to the best of a file-systems capabilities; possibly guaranteeing that there is at most only ever a single writing operating taking place at any given moment per physical hard-disk.

#### Broker via RPC

One possible implementation of a broker is to utilising the Open Metadata library via proxy-methods such as a Remore Procedure Call (RPC).

Clients may call upon an exposed service pass to any data they wish to be written as Open Metadata through it. The recieving end would then manage the actual reads and writes to the file-system(s), thus ensuring that there is only ever one concurrent read and write happening while also being natively adept at queing requests and otherwise handle a gigantic amount of requests.

The broker then would be this service.

### Push/Pull

Similar to the Broker-model, another solution may be to write temporarily to one location, in preparation for the next.

![](../images/13/pushpull.png)

```python
>>> location = om.Location('/server/location')
>>> dataset = om.Dataset('new_data.string', data='a value', parent=location)
>>> om.commit(dataset)
>>> om.push()
```

Here, a dataset is first "committed" to be written publicly, meaning it is written to the local hard-drive; in a common place for metadata written by this user.

```python
/home/marcus/.metastage/server/location/new_data.string
```

Upon om.push(), Open Metadata would look for ".metastage" underneath the calling user's home-directory and schedule that data to be written to a server.

The push-mechanism could then handle concurrency and decide who eventually ends up the latest writing the latest data, and also alert the user when writes happen within a certain time-span, such as within 0.1 microseconds. At that point, the user could reasonably expect his data to having been overwritten by someone else.

It could potentially also be the place where priorities are set on requests. Some users or processes may require their data to always take precedence over others, if that data should so happen to be written within a given time-span.

And ultimately, it would help guarantee that, even though data may be overwritten in one location, it is never lost and can be re-submitted either automatically or manually per a user's request.

### 5. Push/Pull Daemon

One of the advantages over using a proxy for storage as opposed to working directly towards a database is that you can schedule for writes to happen at a time more convenient for writing.

For example, imagine you are working within an application which produces massive amounts of metadata; sporadically streaming to disk at a rate of 100mb/sec, and that it did so only for a few seconds.

If this data were to immediately write to a remote server, the transfer could potentially become a bottle-neck in this process.

Instead, the data could be written locally and a background process, a.k.a daemon, could then time the instances you are attempting to write and only Push once the time in between writes have reached a certain threshold; such as 10 seconds.

Only after 10 seconds of inactivity would the daemon get to work in pushing all of this data onto the server.

The user would get fast response-time, and the server would get one big chunk of data to store, rather than a sporadic cloud of requests.
