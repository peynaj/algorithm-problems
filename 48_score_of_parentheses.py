"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        indexes = {}
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                indexes[stack.pop()] = i

        def helper(open_index):
            if open_index not in indexes:
                return 0
            close_index = indexes[open_index]
            if (open_index + 1) in indexes:
                return 2 * helper(open_index + 1) + helper(close_index + 1)
            return 1 + helper(close_index + 1)

        return helper(0)


test_cases = {
    "()": 1,
    "()()": 2,
    "(())": 2,
    "(()(()))": 6,
}


def run_tests():
    for s, expected in test_cases.items():
        actual = Solution().scoreOfParentheses(s)
        assert actual == expected, f"{s=} {expected=} {actual=}"

    print(f"OK! {len(test_cases)} Test PASS.")


if __name__ == "__main__":
    run_tests()
