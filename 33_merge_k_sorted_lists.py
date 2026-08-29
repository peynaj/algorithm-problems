"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_1_brute_fource(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time: O(n * k * k)
    Space: O(1)
    """
    dummy_head = ListNode(0)
    curr = dummy_head
    while True:
        next_node = None
        next_i = -1
        for i, head in enumerate(lists):
            if head and (next_node is None or head.val < next_node.val):
                next_node = head
                next_i = i
        if next_node is None:
            return dummy_head.next

        lists[next_i] = next_node.next
        next_node.next = None
        curr.next = next_node
        curr = next_node

    return dummy_head.next


def merge_k_lists_2_sort_all_values(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time: O(k * n * log (k * n))
    Space: O(k * n)
    """
    dummy_head = ListNode(0)
    values = []
    for head in lists:
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
    values.sort()
    curr = dummy_head
    for v in values:
        _next = ListNode(v)
        curr.next = _next
        curr = _next

    return dummy_head.next


def merge_k_lists_3_heapq(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time: O(n * log k)
    Space: O(k)
    """
    dummy_head = ListNode(0)
    hq = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(hq, (head.val, i, head))

    curr = dummy_head
    while hq:
        _, i, next_node = heapq.heappop(hq)

        curr.next = next_node
        curr = next_node

        if next_node.next:
            heapq.heappush(hq, (next_node.next.val, i, next_node.next))

    return dummy_head.next


def run_tests():
    solutions = [
        merge_k_lists_1_brute_fource,
        merge_k_lists_2_sort_all_values,
        merge_k_lists_3_heapq,
    ]
    for func in solutions:
        print(func.__name__, "...")
        n1 = ListNode(1)
        n1.next = ListNode(4)
        n1.next.next = ListNode(5)

        n2 = ListNode(1)
        n2.next = ListNode(3)
        n2.next.next = ListNode(4)

        n3 = ListNode(2)
        n3.next = ListNode(6)

        r = func([n1, n2, n3])
        print("Result:")
        curr = r
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print(".")

    print("Done!")


if __name__ == "__main__":
    run_tests()
