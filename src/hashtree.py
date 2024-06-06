import hashlib


class HashTree:
    def __init__(self):
        self.root: Node | None = None
        self.leaves: list[Node] = []

    def add(self, data):
        node = Node(data)
        self.leaves.append(node)
        self.update()

    def update(self):
        if len(self.leaves) == 0:
            self.root = None
            return

        tree_copy = self.leaves
        while len(tree_copy) > 1:
            if len(tree_copy) % 2 == 1:
                tree_copy.append(Node(self.leaves[-1].hash))
            new_node_level = []
            for i in range(0, len(tree_copy), 2):
                new_node = Node(lnode=tree_copy[i], rnode=tree_copy[i + 1])
                new_node_level.append(new_node)
            tree_copy = new_node_level

        self.root = tree_copy[0]
        

class Node:

    def __init__(self, lnode=None, rnode=None, data=None):
        self.LNode = lnode
        self.RNode = rnode
        self.hash = self.HashNode(data)

    def HashNode(self, data):
        if data is None:
            if self.LNode and self.RNode:
                return hashlib.sha256((self.LNode.hash + self.RNode.hash).encode()).hexdigest()
            else:
                return hashlib.sha256(''.encode()).hexdigest()
