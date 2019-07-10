# MapCollection
# Copyright (c) Simon Raichl 2019
# MIT License


class MapCollection:

    __slots__ = ["__values"]

    def __init__(self, iterable=None):
        self.__values = []

        if isinstance(iterable, list):
            for key, value in iterable:
                self.set(key, value)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.delete(key)

    def __get_values(self, entry):
        return list(map(lambda entries: entries[entry], self.__values))

    def clear(self):
        self.__values = []

    def delete(self, key):
        for i, k in enumerate(self.keys()):
            if k == key:
                del self.__values[i]
                return True

        return False

    def entries(self):
        return self.__values

    def foreach(self, callback):
        for entry in self.__values:
            callback(entry)

    def get(self, key):
        for k, value in self.__values:
            if k == key:
                return value

    def has(self, key):
        return bool(self.get(key))

    def keys(self):
        return self.__get_values(0)

    def size(self):
        return len(self.__values)

    def set(self, key, value):
        values = [key, value]

        for i, k in enumerate(self.keys()):
            if k == key:
                self.__values[i] = values
                return self

        self.__values.append(values)
        return self

    def values(self):
        return self.__get_values(1)
