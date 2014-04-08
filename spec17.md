# Cross-referencing Metadata

An extension to Open Metadata to support the notion of cross-referencing.

* Name: http://rfc.abstractfactory.io/spec/17
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft

Copyright, Change Process and Language is derived via inheritance as per RFC1

# Goal

# Exposing encapsulation

Metadata may be exposed so that it may later be referenced by name, rather than via absolute path.

```python
>>> location = om.Location('/home/marcus')
>>> mydata = om.Dataset('mydata.string', data='World', parent=location)
>>> om.dump(mydata)
>>> om.expose(mydata, 'ImportantMessage')
```

At this point, '/home/marcus' will contain an absolute reference to the metadata `mydata.string` by the (unique) name of `ImportantMessage` that may be referenced via children at any level below the current hierarchy.

```python
>>> location = om.Location('/home/marcus/desktop')
>>> somedata = om.Dataset('somedata.string', parent=location)
>>> somedata.data = 'Hello {ImportantMessage}'
'Hello World'
```

# A trustworthy encapsulation

Similar to attribute access within an inheritance tree, referencing is a one-way street. Children MUST be able to access metadata exposed by parents, but parents MUST NOT be able to access metadata exposed by children.

#### This won't work

```python
# Expose data with a child
location = om.Location('/home/marcus')
dataset = om.Dataset('exposed_data.bool', data=True, parent=location)
om.expose(dataset, 'MyExposedData')
```

```python
# Try and referencing it from a parent
>>> location = om.Location('/home')
>>> dataset = om.Dataset('referencing_data.string', parent=location)
>>> dataset.data = 'I love ice-cream: {MyExposedData}'
Exception: Exposed data 'MyExposedData' not found
```

### When exposition conflicts

Since any child within a hierarchy may choose to expose metadata, it is possible for a unique name exposed via a parent to be overwritten by a child. This is perfectly fine in most scenarios as it facilitates a cascading behaviour in attribute access which aligns with RFC12/OOM.

```python
>>> dataset1 = om.Dataset('importantdata.string', parent=parent_location)
>>> dataset2 = om.Dataset('veryimportantdata.string', parent=child_location)
>>> om.expose(dataset1, 'importantUniqueName')
>>> om.expose(dataset2, 'importantUniqueName')
```

However, there may be cases when this MUST NOT be allowed to happen and so the mechanism MUST include a method of asserting this; such as raising an exception or returning an error code either when it is attempted or when multiple names were found upon query.

### Escaping {}

If you encounter a situation where the @-sign necessarily must appear directly infront of a character, you may escape it.

```python
>>> somedata.data = 'Hello \{ImportantMessage\}'
'Hello {ImportantMessage}'
```
