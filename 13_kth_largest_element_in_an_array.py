"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Input:  [1, 23, 12, 9, 30, 2, 50], K = 3
Output: 23

Input:  [12, 3, 5, 7, 19], K = 2
Output: 12
"""

import heapq
import random


def find_kth_largest_1_priority_queue(nums: list[int], k: int) -> int:
    """
    Time: O(n log k)
    Space: O(k)
    """
    top_k = nums[:k]
    heapq.heapify(top_k)
    for x in nums[k:]:
        if x > top_k[0]:
            heapq.heappushpop(top_k, x)
    return top_k[0]


def find_kth_largest_2_quick_select(nums: list[int], k: int) -> int:
    """
    Expected Time: O(n)
    Worst Time: O(n^2)
    Space: O(n)
    """

    def quick_select(arr, k):
        pivot = random.choice(arr)
        left = [x for x in arr if x > pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
        if k <= len(left):
            return quick_select(left, k)
        if len(left) + len(mid) < k:
            return quick_select(right, k - len(left) - len(mid))
        return pivot

    return quick_select(nums, k)


def find_kth_largest_3_counting_sort(nums: list[int], k: int) -> int:
    """
    Time: O(n+R) (R = frequency size)
    Space: O(n)
    """
    range_size = 10 ** 5 + 1
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    count = 0
    for i in range(range_size - 1, -range_size, -1):
        count += freq.get(i, 0)
        if count >= k:
            return i
    return -1


def run_tests():
    for nums, k, expected in [
        [[1, 23, 12, 9, 30, 2, 50], 3, 23],
        [[12, 3, 5, 7, 19], 2, 12],
    ]:
        print(nums, k, expected)
        for solution in [
            find_kth_largest_1_priority_queue,
            find_kth_largest_2_quick_select,
            find_kth_largest_3_counting_sort,
        ]:
            print(solution.__name__, ">")
            res = solution(nums, k)
            assert res == expected, f"{nums=} {k=} {expected=} {res=}"
        print("-" * 80)

    print("Done!")


if __name__ == "__main__":
    run_tests()
