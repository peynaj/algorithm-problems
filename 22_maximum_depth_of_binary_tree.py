"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node
 down to the farthest leaf node.
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_1_bfs(root: Optional[TreeNode]) -> int:
    """
    BFS
    Time: O(n)
    Space: O(w) w = maximum breadth of tree
    """
    if not root:
        return 0

    depth = 0
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        depth += 1
        for _ in range(level_size):
            node = q.popleft()
            for child in [node.left, node.right]:
                if child:
                    q.append(child)

    return depth


def max_depth_2_recursive(root: Optional[TreeNode]) -> int:
    """
    DFS + recursive
    Time: O(n)
    Space: O(h) for recursive stack
    """
    if not root:
        return 0

    return 1 + max(
        max_depth_2_recursive(root.left),
        max_depth_2_recursive(root.right),
    )


def run_tests(solution):
    print(f"Solution: {solution.__name__}")
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    depth = solution(root)
    assert depth == 3, f"{depth=}"

    assert solution(None) == 0

    print("Done!")


if __name__ == "__main__":
    for solution in [
        max_depth_1_bfs,
        max_depth_2_recursive,
    ]:
        run_tests(solution)
