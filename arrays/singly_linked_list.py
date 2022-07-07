from typing import Any


class SinglyLinkedNode:
    def __init__(self, data: Any):
        self.value = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head: SinglyLinkedNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def at(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def push_front(self, value: Any) -> 'SinglyLinkedList':
        new_node = SinglyLinkedNode(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        return self

    def pop_front(self) -> Any:
        if self.is_empty():
            raise IndexError
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def push_back(self, value: Any) -> 'SinglyLinkedList':
        new_node = SinglyLinkedNode(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1
        return self

    def pop_back(self) -> Any:
        if self.is_empty():
            raise IndexError
        if self._size == 1:
            value = self.head.value
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            value = current.next.value
            current.next = None
        self._size -= 1
        return value

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError
        return self.head.value

    def back(self) -> Any:
        if self.is_empty():
            raise IndexError
        current = self.head
        while current.next is not None:
            current = current.next
        return current.value

    def insert(self, index: int, value: Any) -> 'SinglyLinkedList':
        if index < 0 or index > self._size:
            raise IndexError
        new_node = SinglyLinkedNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1
        return self

    def erase(self, index: int) -> 'SinglyLinkedList':
        if index < 0 or index >= self._size:
            raise IndexError
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self._size -= 1
        return self

    def value_n_from_end(self, n: int) -> Any:
        if n < 0 or n > self._size:
            raise IndexError
        current = self.head
        for _ in range(self._size - n):
            current = current.next
        return current.value

    # noinspection PyShadowingBuiltins
    def reverse(self) -> 'SinglyLinkedList':
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self

    def remove_value(self, value: Any) -> 'SinglyLinkedList':
        if self.is_empty():
            raise IndexError
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next
        self._size -= 1
        return self

    def __str__(self) -> str:
        current = self.head
        s = ''
        while current is not None:
            s += str(current.value) + ' '
            current = current.next
        return s
