"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
 by continuously following the next pointer.
 Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
 Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def detect_cycle_1_hash_set(head: Node) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    s = set()
    curr = head
    while curr is not None:
        if curr in s:
            return True
        s.add(curr)
        curr = curr.next
    return False


def detect_cycle_2_floyd_cycle(head: Node) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


def run_tests():
    for solution in [
        detect_cycle_1_hash_set,
        detect_cycle_2_floyd_cycle,
    ]:
        print(solution.__name__, ">")
        print("test 1")
        head = Node(1)
        head.next = Node(3)
        head.next.next = Node(4)
        head.next.next.next = head.next
        assert solution(head)

        print("test 2")
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        assert not solution(head)

        print("test 3")
        head = Node(1)
        head.next = head
        assert solution(head)

        print("test 4")
        head = Node(1)
        assert not solution(head)

        print("-" * 80)

    print("Done!")


if __name__ == "__main__":
    run_tests()
