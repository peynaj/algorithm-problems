"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
 that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor_1_store_path(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    parents = {}
    s = [root]
    while s:
        curr = s.pop()
        for child in [curr.left, curr.right]:
            if child:
                parents[child.val] = curr
                s.append(child)

    path1 = [p]
    anc = parents.get(p.val)
    while anc:
        path1.append(anc)
        anc = parents.get(anc.val)

    path2 = [q]
    anc = parents.get(q.val)
    while anc:
        path2.append(anc)
        anc = parents.get(anc.val)

    res = None
    while path1 and path2 and path1[-1].val == path2[-1].val:
        res = path1.pop()
        path2.pop()

    return res


def lowest_common_ancestor_2_single_traversal(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(h) -> recursion stack
    """
    lca = lowest_common_ancestor_2_single_traversal

    if not root:
        return None

    if root == p or root == q:
        return root
    left_lca = lca(root.left, p, q)
    right_lca = lca(root.right, p, q)
    if left_lca and right_lca:
        return root
    return left_lca or right_lca
