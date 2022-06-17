import unittest

from arrays.vector import Vector


class TestVector(unittest.TestCase):
    def test_size(self):
        vec = Vector()
        self.assertEqual(vec.is_empty(), True)

        vec.push(1).push(2).push(3)
        self.assertEqual(vec.is_empty(), False)

        self.assertEqual(vec.size(), 3)
        vec.pop()
        self.assertEqual(vec.size(), 2)

    def test_capacity(self):
        vec = Vector()
        self.assertEqual(vec.capacity(), 16)
        vec.push(0).push(0).push(0).push(1) \
            .push(1).push(1).push(1).push(1) \
            .push(1).push(1).push(1).push(1) \
            .push(1).push(1).push(1).push(1)
        self.assertEqual(vec.capacity(), 32)

        vec.remove(1)
        vec.push(1)
        self.assertEqual(vec.capacity(), 16)

    def test_at(self):
        vec = Vector()
        with self.assertRaises(IndexError):
            vec.at(0)
        with self.assertRaises(IndexError):
            vec.at(-1)

        vec.push(1)
        self.assertEqual(vec.at(0), 1)

    def test_push(self):
        vec = Vector()
        vec.push(1)
        self.assertEqual(vec.at(0), 1)
        self.assertEqual(vec.size(), 1)
        self.assertEqual(vec.capacity(), 16)

    def test_insert(self):
        vec = Vector()
        with self.assertRaises(IndexError):
            vec.insert(1, 1)
        with self.assertRaises(IndexError):
            vec.insert(-1, 1)

        vec.push(1).push(2).push(3)
        vec.insert(1, 4)
        self.assertEqual(str(vec), '[1, 4, 2, 3]')
        self.assertEqual(vec.size(), 4)
        self.assertEqual(vec.capacity(), 16)

        vec.insert(0, 5)
        self.assertEqual(str(vec), '[5, 1, 4, 2, 3]')
        self.assertEqual(vec.size(), 5)
        self.assertEqual(vec.capacity(), 16)

        vec.insert(4, 6)
        self.assertEqual(str(vec), '[5, 1, 4, 2, 6, 3]')
        self.assertEqual(vec.size(), 6)
        self.assertEqual(vec.capacity(), 16)

    def test_prepend(self):
        vec = Vector()
        vec.prepend(3)
        self.assertEqual(str(vec), '[3]')

        vec.prepend(2)
        self.assertEqual(str(vec), '[2, 3]')
        self.assertEqual(vec.size(), 2)
        self.assertEqual(vec.capacity(), 16)

    def test_pop(self):
        vec = Vector()
        with self.assertRaises(IndexError):
            vec.pop()

        vec.push(1)
        self.assertEqual(vec.pop(), 1)
        self.assertEqual(vec.size(), 0)
        self.assertEqual(vec.capacity(), 16)

    def test_delete(self):
        vec = Vector()
        with self.assertRaises(IndexError):
            vec.delete(0)
        with self.assertRaises(IndexError):
            vec.delete(-1)
        with self.assertRaises(IndexError):
            vec.delete(1)

    def test_remove(self):
        vec = Vector()
        with self.assertRaises(ValueError):
            vec.remove(0)
        with self.assertRaises(ValueError):
            vec.remove(-1)
        with self.assertRaises(ValueError):
            vec.remove(1)

        vec.push(1).push(2).push(3)
        vec.remove(2)
        self.assertEqual(str(vec), '[1, 3]')
        self.assertEqual(vec.size(), 2)
        self.assertEqual(vec.capacity(), 16)

        vec.remove(1)
        vec.remove(3)
        self.assertEqual(str(vec), '[]')
        self.assertEqual(vec.size(), 0)
        self.assertEqual(vec.capacity(), 16)

    def test_find(self):
        vec = Vector()
        self.assertEqual(vec.find(1), -1)
        vec.push(1).push(2).push(3)

        self.assertEqual(vec.find(1), 0)
        self.assertEqual(vec.find(2), 1)
        self.assertEqual(vec.find(3), 2)
        self.assertEqual(vec.find(4), -1)

    def test_clear(self):
        vec = Vector()
        vec.push(1).push(2).push(3)
        vec.clear()
        self.assertEqual(str(vec), '[]')
        self.assertEqual(vec.size(), 0)
        self.assertEqual(vec.capacity(), 16)
