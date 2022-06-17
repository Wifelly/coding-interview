from typing import Any


class Vector:
    def __init__(self, capacity: int = 16):
        self._capacity = capacity
        self._arr = [None] * capacity
        self._size = 0

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False

    def at(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError
        return self._arr[index]

    def push(self, value: Any) -> 'Vector':
        self._arr[self._size] = value
        self._size += 1
        self._ensure_capacity()
        return self

    def insert(self, index: int, value: Any) -> 'Vector':
        if 0 > index or index > self._size:
            raise IndexError
        for item in range(self._size, index, -1):
            self._arr[item] = self._arr[item - 1]
        self._arr[index] = value
        self._size += 1
        self._ensure_capacity()
        return self

    def prepend(self, value: Any) -> 'Vector':
        for item in range(self._size, 0, -1):
            self._arr[item] = self._arr[item - 1]
        self._arr[0] = value
        self._size += 1
        self._ensure_capacity()
        return self

    def pop(self) -> Any:
        if self._size == 0:
            raise IndexError
        value = self._arr[self._size - 1]
        self._arr[self._size - 1] = None
        self._size -= 1
        return value

    def delete(self, index: int) -> 'Vector':
        if index < 0 or index >= self._size:
            raise IndexError
        self._arr[index] = None
        for item in range(index, self._size - 1):
            self._arr[item] = self._arr[item + 1]
        self._size -= 1
        return self

    def remove(self, value: Any) -> 'Vector':
        index = self.find(value)
        if index == -1:
            raise ValueError
        for item in range(self._size - 1, 0 - 1, -1):
            if self._arr[item] == value:
                self.delete(item)
        return self

    def clear(self) -> 'Vector':
        self._arr = [None] * self._capacity
        self._size = 0
        return self

    def find(self, value: Any) -> Any:
        for item in range(self._size):
            if self._arr[item] == value:
                return item
        return -1

    def _resize(self, new_capacity: int) -> 'Vector':
        new_arr = [None] * new_capacity
        for item in range(self._size):
            new_arr[item] = self._arr[item]
        self._arr = new_arr
        self._capacity = new_capacity
        return self

    def _ensure_capacity(self) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        if self._capacity > 16 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)

    def __str__(self) -> str:
        return str(self._arr[:self._size])

    def __repr__(self) -> str:
        return str(self._arr)

