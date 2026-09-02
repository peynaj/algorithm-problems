"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def reverse_list_1_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(1)
    """
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        curr, prev = next_node, curr

    return prev


def reverse_list_2_recursion(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(n)
    """
    if head is None or head.next is None:
        return head
    rest = reverse_list_2_recursion(head.next)
    head.next.next = head
    head.next = None
    return rest


def reverse_list_3_stack(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(n)
    """
    if head is None:
        return None
    stack = []
    temp = head
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next

    result = temp
    while stack:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None

    return result


def print_list(node):
    while node is not None:
        print(node.data, end=" -> " if node.next else "")
        node = node.next
    print()


def run_tests():
    for solution in [
        reverse_list_1_iterative,
        reverse_list_2_recursion,
        reverse_list_3_stack,
    ]:
        print(solution.__name__, ">")
        head = ListNode(1)
        curr = head
        for i in range(2, 10):
            curr.next = ListNode(i)
            curr = curr.next

        print("Linked List:")
        print_list(head)
        result = solution(head)
        print("Reversed:")
        print_list(result)
        print("-" * 80)


if __name__ == "__main__":
    run_tests()
