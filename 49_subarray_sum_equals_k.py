"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Hash map and Prefix sum
        Time: O(n)
        Space: O(n)
        """
        count = 0
        prefix_sum = {0: 1}
        curr_sum = 0
        for x in nums:
            curr_sum += x
            count += prefix_sum.get(curr_sum - k, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return count


test_cases = [
    # nums, k, expected
    ([1, 1, 1], 2, 2),
    ([1, 1, 1], 2, 2),
    ([10, 2, -2, -20, 10], -10, 3),
    ([9, 4, 20, 3, 10, 5], 33, 2),
    ([1, 3, 5], 2, 0),
    ([0, 0, 0], 0, 6),
    ([1], 1, 1),
    ([1], 0, 0),
    ([-1, -1, 1], 0, 1),
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ([1, -1, 0], 0, 3),
]


def run_tests():
    for nums, k, expected in test_cases:
        actual = Solution().subarraySum(nums, k)
        assert actual == expected, f"{nums=} {k=} {expected=} {actual=}"

    print(f"OK! {len(test_cases)} Test PASS.")


if __name__ == "__main__":
    run_tests()
