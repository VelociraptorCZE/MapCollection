# MapCollection

MapCollection is basically port from JavaScript Map object for Python.
It has same set of functions as Map and also works in nearly the same way.
It's worth mention that every key is unique like in JS Map and
also you can rewrite values.

In JavaScript you can't use indexers to read, write or remove values from Map, 
however this feature is supported by MapCollection.

### Import

```python
from MapCollection import MapCollection
```

### Constructor

You can pass through constructor an iterable as the initial
values.

```python
mapCollection = MapCollection([[3.14, "PI"], [2.71, "E"], [3.14, "Overwritten PI"]])
```

### clear()

Clears MapCollection, returns None.

```python
mapCollection.clear()
```

### delete(key)

Removes particular key from MapCollection, returns True or False whether the entry by supplied key was actually removed.

```python
mapCollection.delete("someKey")
```

Or:

```python
del mapCollection["someKey"]
```

### entries()

Returns all entries in array.

```python
mapCollection.entries()
```

### foreach(callback)

Iterable function, returns None:

```python
mapCollection.foreach(lambda entry: print("Entry from MapCollection", entry))
```

### get(key)

Returns value selected by key from MapCollection or None if key wasn't found.

```python
mapCollection.get("someKey")
```

Alternatively: 

```python
mapCollection["someKey"]
```

### has(key)

Returns True or False whether the key was found in MapCollection.

```python
mapCollection.has("someKey")
```

### keys()

Returns all keys as array.

```python
mapCollection.keys()
```

### size()

Returns number of values in MapCollection instance.

```python
mapCollection.size()
```

### set(key, value)

Sets a value alongside key or replaces value if key is already present in MapCollection also
returns current MapCollection instance so you can chain **set** function if you want to add multiple values on one line.

```python
mapCollection.set(50, 100)
```

In addition you can set also value by indexer:

```python
mapCollection[50] = 100
```

### values()

Returns all values in array.

```python
mapCollection.values()
```