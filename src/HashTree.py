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
