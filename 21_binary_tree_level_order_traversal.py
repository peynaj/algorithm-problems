"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal_1_bfs(root: Optional[TreeNode]) -> list[list[int]]:
    """
    Breadth First Search
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []

    result = []
    q = deque()
    q.append(root)
    while q:
        level = []
        q_len = len(q)
        for _ in range(q_len):
            node = q.popleft()
            level.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append(child)

        result.append(level)
    return result


def level_order_rec(root: Optional[TreeNode], level: int, result: list[list[int]]):
    if not root:
        return
    if len(result) <= level:
        result.append([])
    result[level].append(root.val)
    level_order_rec(root.left, level+1, result)
    level_order_rec(root.right, level + 1, result)
    return


def level_order_traversal_2_recursive(root: Optional[TreeNode]) -> list[list[int]]:
    """
    DFS + level tracking
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    result = []
    level_order_rec(root, 0, result)
    return result


def run_tests(solution):
    print(f"Solution: {solution.__name__}")
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    level_order = solution(root)
    print(1, level_order)
    assert len(level_order) == 3
    assert level_order[0] == [3]
    assert level_order[1] == [9, 20]
    assert level_order[2] == [15, 7]

    root = TreeNode(1)
    level_order = solution(root)
    print(2, level_order)
    assert len(level_order) == 1
    assert level_order[0] == [1]

    root = None
    level_order = solution(root)
    print(3, level_order)
    assert len(level_order) == 0

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    level_order = solution(root)
    print(4, level_order)
    assert len(level_order) == 5
    assert level_order == [[1], [2], [3], [4], [5]]

    print("-" * 80)


if __name__ == "__main__":
    for solution in [
        level_order_traversal_1_bfs,
        level_order_traversal_2_recursive,
    ]:
        run_tests(solution)

    print("Done!")
