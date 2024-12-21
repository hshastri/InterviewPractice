from collections import deque
from typing import Dict


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None

class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode = None

    def insert(self, val: int):
        self.root = self._insert_into_bst(self.root, val)

    def _insert_into_bst(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self._insert_into_bst(root.left, val)
        else:
            root.right = self._insert_into_bst(root.right, val)

        return root

    def find(self, val: int) -> bool:
        return self._find_rec(self.root, val)

    def _find_rec(self, current: TreeNode, val: int) -> bool:
        if current is None:
            return False
        if current.val == val:
            return True
        elif val < current.val:
            return self._find_rec(current.left, val)
        else:
            return self._find_rec(current.right, val)

    def print_in_order(self):
        self._print_in_order_rec(self.root)

    def _print_in_order_rec(self, current: TreeNode):
        if current is not None:
            self._print_in_order_rec(current.left)
            print(current.val)
            self._print_in_order_rec(current.right)

    def bfs(self) -> Dict[str, int]:
        nodes = deque([self.root])
        current_level = 0
        levels = {tuple([str(node.val) for node in nodes]): current_level}
        while nodes:
            for i in range(len(nodes)):
                current = nodes.popleft()
                if current.left:
                    nodes.append(current.left)
                if current.right:
                    nodes.append(current.right)
            current_level += 1
            if nodes:
                levels[tuple([str(node.val) for node in nodes])] = current_level
        return levels


def main():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(7)

    print("In-order traversal:")
    bst.print_in_order()

    print("\nFind results:")
    print(f"Find 7: {bst.find(7)}")  # Should return True
    print(f"Find 12: {bst.find(12)}")  # Should return False

    print(bst.root.val)
    print("BFS levels")
    print(bst.bfs())

    """In-order traversal:
    5
    7
    10
    15
    
    Find results:
    Find 7: True
    Find 12: False
    10
    BFS levels:
    {('10',): 0, ('5', '15'): 1, ('7',): 2}
    
        10
       /  \
      5   15
       \
        7
    """

if __name__ == '__main__':
    main()
