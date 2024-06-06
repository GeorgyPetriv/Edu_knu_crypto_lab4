from unittest import TestCase
from src.hashtree import HashTree, Node


class TestHashtree(TestCase):
    def test_constructor(self):
        htree = HashTree()
        self.assertEqual(0, len(htree.leaves), "Leaves are not empty")
        self.assertIsNone(htree.root, "Root is not none")

    def test_add_leaf(self):
        htree = HashTree()
        test_node = Node('test data')

        htree.add(test_node)
        self.assertIsNotNone(htree.root, "Root is none")
        self.assertEqual(1, len(htree.leaves), "Leaves are empty")