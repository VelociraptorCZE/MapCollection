# MapCollection
# Copyright (c) Simon Raichl 2019
# MIT License


class MapCollection:

    __values = []

    def __init__(self, iterable=None):
        if not isinstance(iterable, list):
            iterable = []
        for key, value in iterable:
            self.set(key, value)

    def __get_values(self, entry):
        return list(map(lambda entries: entries[entry], self.__values))

    def clear(self):
        self.__values = []

    def delete(self, key):
        i = 0
        for entry in self.__values:
            if entry[0] == key:
                del self.__values[i]
                return True
            i += 1

        return False

    def entries(self):
        return self.__values

    def foreach(self, callback):
        for entry in self.__values:
            callback(entry)

    def get(self, key):
        for entry in self.__values:
            if entry[0] == key:
                return entry[1]

    def has(self, key):
        return bool(self.get(key))

    def keys(self):
        return self.__get_values(0)

    def size(self):
        return len(self.__values)

    def set(self, key, value):
        i = 0
        values = [key, value]

        for k, _ in self.__values:
            if k == key:
                self.__values[i] = values
                return self
            i += 1

        self.__values.append(values)
        return self

    def values(self):
        return self.__get_values(1)
