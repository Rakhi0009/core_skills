class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self,root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root
    