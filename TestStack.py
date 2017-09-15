import unittest
from Stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        self.stack.push(42)
        self.stack.push((1,2,3))
        self.stack.pop()

    def test_size(self):
        self.assertEqual(self.stack.size(), 4)

    def test_empty(self):
        self.assertFalse(self.stack.isEmpty())

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 42)

    def tearDown(self):
        self.stack = None

if __name__ == '__main__':
    unittest.main()
