"""
Given the heads of two sorted linked lists,
 merge them into a single sorted linked list and return the head of the merged list.
"""


class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def merge_sorted_lists(head1: ListNode, head2: ListNode) -> ListNode:
    """
    Time: O(n+m)
    Space: O(1)
    """
    dummy = ListNode(None)
    curr = dummy

    while head1 and head2:
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    curr.next = head1 or head2
    return dummy.next


def print_linked_list(head: ListNode):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "")
        curr = curr.next
    print()


def run_tests():
    head1 = ListNode(5)
    head1.next = ListNode(10)
    head1.next.next = ListNode(15)
    head1.next.next.next = ListNode(40)
    print("List 1:")
    print_linked_list(head1)

    head2 = ListNode(2)
    head2.next = ListNode(3)
    head2.next.next = ListNode(20)
    print("List 2:")
    print_linked_list(head2)

    merged_head = merge_sorted_lists(head1, head2)
    print("Merged List:")
    print_linked_list(merged_head)
    print("-" * 80)

    head1 = ListNode(1)
    head1.next = ListNode(10)
    head1.next.next = ListNode(30)
    head1.next.next.next = ListNode(60)
    print("List 1:")
    print_linked_list(head1)

    head2 = ListNode(2)
    head2.next = ListNode(3)
    head2.next.next = ListNode(61)
    print("List 2:")
    print_linked_list(head2)

    merged_head = merge_sorted_lists(head1, head2)
    print("Merged List:")
    print_linked_list(merged_head)
    print("-" * 80)

    print("Done!")


if __name__ == "__main__":
    run_tests()
