from typing import Any


class DoubleLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head: DoubleLinkedNode | None = None
        self.tail: DoubleLinkedNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def at(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError
        if index > self._size // 2:
            current = self.tail
            for _ in range(self._size - index - 1):
                current = current.prev
            return current.data
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data

    def push_front(self, value: Any) -> 'DoubleLinkedList':
        new_node = DoubleLinkedNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
        return self

    def pop_front(self) -> Any:
        if self.is_empty():
            raise IndexError
        value = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self._size -= 1
        return value

    def push_back(self, value: Any) -> 'DoubleLinkedList':
        new_node = DoubleLinkedNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return self

    def pop_back(self) -> Any:
        if self.is_empty():
            raise IndexError
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        self._size -= 1
        return value

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError
        return self.head.data

    def back(self) -> Any:
        if self.is_empty():
            raise IndexError
        return self.tail.data

    def insert(self, index: int, value: Any) -> 'DoubleLinkedList':
        if index < 0 or index > self._size:
            raise IndexError
        if index == 0:
            self.push_front(value)
        elif index == self._size:
            self.push_back(value)
        else:
            new_node = DoubleLinkedNode(value)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self._size += 1
        return self

    def erase(self, index: int) -> 'DoubleLinkedList':
        if index < 0 or index >= self._size:
            raise IndexError
        if index == 0:
            self.pop_front()
        elif index == self._size - 1:
            self.pop_back()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self._size -= 1
        return self

    def value_n_from_end(self, index: int) -> Any:
        if index < 0 or index > self._size:
            raise IndexError
        current = self.tail
        for _ in range(self._size - index):
            current = current.prev
        return current.data

    def reverse(self) -> 'DoubleLinkedList':
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            current = next_node
        self.head, self.tail = self.tail, self.head
        return self

    def remove_value(self, value: Any) -> 'DoubleLinkedList':
        current = self.head
        while current is not None:
            if current.data == value:
                if current == self.head:
                    self.pop_front()
                elif current == self.tail:
                    self.pop_back()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self._size -= 1
            current = current.next
        return self

    def __str__(self):
        current = self.head
        string = ''
        while current is not None:
            string += str(current.data) + ' '
            current = current.next
        return string
