"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of
 all the values of the nodes in the tree.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode], result: list):
    if not root:
        return
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)


def kth_smallest_1_inorder_traversal(root: Optional[TreeNode], k: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    sorted_values = []
    inorder(root, sorted_values)
    return sorted_values[k - 1]


def kth_smallest_2_morris_traversal(root: Optional[TreeNode], k: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    Extra Space: O(1)
    """
    count = 0
    curr = root
    while curr:
        if curr.left is None:
            # visit and go right
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
        else:
            # find predecessor
            predecessor = curr.left
            while predecessor.right and predecessor.right != curr:
                predecessor = predecessor.right

            if predecessor.right is None:
                # create thread and go left
                predecessor.right = curr
                curr = curr.left
            else:
                # clear thread
                predecessor.right = None
                # visit and go right
                count += 1
                if count == k:
                    return curr.val
                curr = curr.right


def run_test():
    for kth_smallest in [
        kth_smallest_1_inorder_traversal,
        kth_smallest_2_morris_traversal,
    ]:
        print(f"Solution: {kth_smallest.__name__}")
        print("Test 1")
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)

        k = 3
        expected = 3
        result = kth_smallest(root, k)
        assert result == expected, f"{expected=}, {result=}"

        print("Test 2")
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)
        k = 1
        expected = 1
        result = kth_smallest(root, k)
        assert result == expected, f"{expected=}, {result=}"

        print("Test 3")
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)
        k = 6
        expected = 6
        result = kth_smallest(root, k)
        assert result == expected, f"{expected=}, {result=}"

        print("OK!")


if __name__ == "__main__":
    run_test()
