"""
Given a string s containing three types of brackets {}, () and [].
 Determine whether the Expression are balanced or not.
 An expression is balanced if each opening bracket has a corresponding closing bracket of the same type,
 the pairs are properly ordered and no bracket closes before its matching opening bracket.

Balanced: "[()()]{}" → every opening bracket is closed in the correct order.
Not balanced: "([{]})" → the ']' closes before the matching '{' is closed, breaking the nesting rule.
"""


def valid_parentheses_1_stack(s: str) -> bool:
    """
    Space: O(n)
    Time: O(n)
    """
    parentheses_map = {")": "(", "]": "[", "}": "{"}
    opening = tuple(parentheses_map.values())
    stack = []
    for c in s:
        if c in opening:
            stack.append(c)
        elif c in ")}]":
            if not stack or stack[-1] != parentheses_map.get(c):
                return False
            stack.pop()

    return not bool(stack)


# =============================== Test =========================

solutions = [
    valid_parentheses_1_stack,
]

test_cases = [
    "",
    "{",
    "[{()}]",
    "[{(a)}]",
    "([{]})",
    "()[]{}",
]

for i, test in enumerate(test_cases):
    print(i, test)
    for func in solutions:
        print(func(test))
    print("-" * 80)
