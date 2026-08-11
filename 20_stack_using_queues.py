"""
Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
"""
from collections import deque


class MyStack:
    """
    Push: O(1)
    Pop: O(n)
    Top: O(n)
    Empty: O(1)
    """

    queue1: deque
    queue2: deque

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue1:
            return -1
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        last = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return last

    def top(self) -> int:
        if not self.queue1:
            return -1
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        last = self.queue1.popleft()
        self.queue2.append(last)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return last

    def empty(self) -> bool:
        return not self.queue1


def run_tests():
    my_stack = MyStack()
    assert my_stack.empty()
    assert my_stack.top() == -1
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    assert my_stack.top() == 3
    assert my_stack.pop() == 3
    assert my_stack.top() == 2
    assert my_stack.pop() == 2
    assert not my_stack.empty()
    assert my_stack.pop() == 1
    assert my_stack.empty()

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
