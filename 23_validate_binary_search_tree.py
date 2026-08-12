"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

"""
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_recursive(node: Optional[TreeNode], min_value: int, max_value: int) -> bool:
    if not node:
        return True
    if not min_value <= node.val <= max_value:
        return False
    return bool(
        bst_recursive(node.left, min_value, node.val - 1)
        and
        bst_recursive(node.right, node.val + 1, max_value)
    )


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    DFS + Recursive
    Time: O(n)
    Space: O(n) -> recursive stack
    """
    if not root:
        return True
    max_constraint = 2 ** 31 + 10
    return bst_recursive(root, -max_constraint, max_constraint)

# TODO: Inorder Traversal

# TODO: Morris Traversal

# =========================================================================================


def run_tests():
    print("Test 1")
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert is_valid_bst(root)

    print("Test 2")
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert not is_valid_bst(root)

    print("Test 3")
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    assert not is_valid_bst(root)

    print("Done!")


if __name__ == "__main__":
    run_tests()
