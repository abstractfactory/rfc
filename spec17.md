# Cross-referencing Metadata

An extension to Open Metadata to support the notion of cross-referencing.

* Name: https://github.com/abstract-factory/rfc/spec:12 (12/OOM)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: RFC1
* State: draft

Copyright, Change Process and Language is derived via inheritance as per [RFC1][].

# Goal



# Expose

Metadata may be exposed so that it may later be referenced by name, rather than via absolute path.

```python
>>> location = om.Location('/home/marcus')
>>> mydata = om.Dataset('mydata.string', data='World', parent=location)
>>> om.dump(mydata)
>>> om.expose(mydata, 'ImportantMessage')
```

At this point, '/home/marcus' will contain an absolute reference to the metadata `mydata.string` by the (unique) name of `ImportantMessage` that may be referenced via any contained children.

```python
>>> location = om.Location('/home/marcus/desktop')
>>> somedata = om.Dataset('somedata.string', parent=location)
>>> somedata.data = 'Hello @ImportantMessage'
'Hello World'
```

### Escaping @

If you encounter a situation where the @-sign necessarily must appear directly infront of a character, you may escape it.

```python
>>> somedata.data = 'Hello \@ImportantMessage'
'Hello @ImportantMessage'
```