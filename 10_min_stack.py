"""
Design a SpecialStack that supports push(x), pop(), peek(), and getMin() in O(1) time.

push(x) → add element x
pop() → remove top element
peek() → return top element without removing; -1 if empty
getMin() → return minimum element; -1 if empty
All operations run in O(1).
"""


class MinStackWithTwoStack:
    """
    Time: O(1)
    Space: O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        if not self.stack:
            return -1
        top = self.stack.pop()
        self.min_stack.pop()
        return top

    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def get_min(self):
        if not self.stack:
            return -1
        return self.min_stack[-1]


class MinStackWithEncodedValues:
    """
    Time: O(1)
    Extra Space: O(1)
    Total Space: O(n)
    """

    def __init__(self):
        self._min = -1
        self.stack = []

    def _encode(self, x):
        return 2 * x - self._min

    def _decode(self, top):
        return 2 * self._min - top

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self._min = x
            return
        if x < self._min:
            self.stack.append(self._encode(x))
            self._min = x
        else:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        top = self.stack.pop()
        res = self._min if top < self._min else top
        if top < self._min:
            self._min = self._decode(top)
        if not self.stack:
            self._min = -1
        return res

    def peek(self):
        if not self.stack:
            return -1
        top = self.stack[-1]
        if top < self._min:
            return self._min
        else:
            return top

    def get_min(self):
        if not self.stack:
            return -1
        return self._min


def run_tests():
    solutions = [
        MinStackWithTwoStack,
        MinStackWithEncodedValues,
    ]
    for solution_class in solutions:
        print(solution_class.__name__)
        min_stack = solution_class()
        assert min_stack.peek() == -1
        assert min_stack.get_min() == -1

        min_stack.push(5)
        min_stack.push(6)
        min_stack.push(7)

        assert min_stack.peek() == 7, min_stack.peek()
        assert min_stack.get_min() == 5

        min_stack.push(1)
        assert min_stack.peek() == 1, min_stack.peek()
        assert min_stack.get_min() == 1

        min_stack.pop()
        assert min_stack.peek() == 7, min_stack.peek()
        assert min_stack.get_min() == 5

        min_stack.pop()
        assert min_stack.peek() == 6, min_stack.peek()
        assert min_stack.get_min() == 5

        min_stack.pop()
        assert min_stack.peek() == 5, min_stack.peek()
        assert min_stack.get_min() == 5

        min_stack.pop()
        assert min_stack.peek() == -1, min_stack.peek()
        assert min_stack.get_min() == -1

        min_stack.push(5)
        min_stack.push(5)
        min_stack.push(5)
        assert min_stack.get_min() == 5

        min_stack.pop()
        assert min_stack.get_min() == 5

        print("-" * 10, "OK")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
