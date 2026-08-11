"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end_1_stack(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(n)
    """
    if head is None or (head.next is None and n == 1):
        return None
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next

    while n:
        stack.pop()
        n -= 1

    if not stack:
        return head.next

    prev_of_target = stack[-1]
    prev_of_target.next = prev_of_target.next.next
    return head


def remove_nth_from_end_2_remove_from_front(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(1)
    """
    if head is None or (head.next is None and n == 1):
        return None

    c = 0
    curr = head
    while curr:
        c += 1
        curr = curr.next

    k = c - n
    if k == 0:
        return head.next
    prev_of_target = head
    while k > 1:
        prev_of_target = prev_of_target.next
        k -= 1
    prev_of_target.next = prev_of_target.next.next
    return head


def remove_nth_from_end_3_slow_and_fast_pointers(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(-1, head)
    slow = dummy
    fast = dummy
    for i in range(n+1):
        if fast is None:
            return head
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    if slow.next:
        slow.next = slow.next.next

    return dummy.next


def print_linked_list(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()


def run_tests():
    solutions = [
        remove_nth_from_end_1_stack,
        remove_nth_from_end_2_remove_from_front,
        remove_nth_from_end_3_slow_and_fast_pointers,
    ]
    print("test 1")
    for func in solutions:
        print(func.__name__, ":")
        head = ListNode(1)
        head.next = ListNode(2)
        n = 2
        print(f"{n=}, List:")
        print_linked_list(head)
        print("Result:")
        print_linked_list(func(head, n))

    print("-" * 80)

    print("test 2")
    for func in solutions:
        print(func.__name__, ":")
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        n = 3
        print(f"{n=}, List:")
        print_linked_list(head)
        print("Result:")
        print_linked_list(func(head, n))

    print("-" * 80)

    print("Done!")


if __name__ == "__main__":
    run_tests()
