import unittest

from arrays.singly_linked_list import SinglyLinkedList, SinglyLinkedNode


class TestSinglyLinkedList(unittest.TestCase):
    def test_size(self):
        list = SinglyLinkedList()
        self.assertEqual(list.is_empty(), True)

        list.push_front(1).push_front(2).push_front(3)
        self.assertEqual(list.is_empty(), False)

        self.assertEqual(list.size(), 3)
        list.pop_front()
        self.assertEqual(list.size(), 2)

    def test_at(self):
        list = SinglyLinkedList()
        with self.assertRaises(IndexError):
            list.at(0)
        with self.assertRaises(IndexError):
            list.at(-1)

        list.push_front(1)
        self.assertEqual(list.at(0), 1)

    def test_push(self):
        list = SinglyLinkedList()
        list.push_front(1)
        self.assertEqual(list.at(0), 1)
        self.assertEqual(list.size(), 1)

    def test_push_back(self):
        list = SinglyLinkedList()
        list.push_back(1)
        self.assertEqual(list.at(0), 1)
        self.assertEqual(list.size(), 1)

        list.push_back(2)
        self.assertEqual(list.at(1), 2)
        self.assertEqual(list.size(), 2)

    def test_pop(self):
        list = SinglyLinkedList()
        list.push_front(1).push_front(2).push_front(3)
        self.assertEqual(list.size(), 3)
        list.pop_front()
        self.assertEqual(list.size(), 2)
        list.pop_front()
        self.assertEqual(list.size(), 1)
        list.pop_front()
        self.assertEqual(list.size(), 0)
        with self.assertRaises(IndexError):
            list.pop_front()

    def test_pop_back(self):
        list = SinglyLinkedList()
        list.push_back(1).push_back(2).push_back(3)
        self.assertEqual(list.size(), 3)
        list.pop_back()
        self.assertEqual(list.size(), 2)
        list.pop_back()
        self.assertEqual(list.size(), 1)
        list.pop_back()
        self.assertEqual(list.size(), 0)
        with self.assertRaises(IndexError):
            list.pop_back()

    def test_insert(self):
        list = SinglyLinkedList()
        with self.assertRaises(IndexError):
            list.insert(1, 1)
        with self.assertRaises(IndexError):
            list.insert(-1, 1)

        list.push_front(1).push_front(2).push_front(3)
        list.insert(1, 4)
        self.assertEqual(str(list), '3 4 2 1 ')
        self.assertEqual(list.size(), 4)

        list.insert(0, 5)
        self.assertEqual(str(list), '5 3 4 2 1 ')
        self.assertEqual(list.size(), 5)

        list.insert(4, 6)
        self.assertEqual(str(list), '5 3 4 2 6 1 ')
        self.assertEqual(list.size(), 6)
