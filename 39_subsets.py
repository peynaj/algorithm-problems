"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""


def subsets_1_backtrack(nums: list[int]) -> list[list[int]]:
    """
    Time: O(n * 2^n)
    Auxiliary Space: O(n)
    Output Space: O(n * 2^n)
    """
    def backtrack(i, subset):
        if i == len(nums):
            ans.append(list(subset))
            return
        # include i
        subset.append(nums[i])
        backtrack(i + 1, subset)
        # exclude i
        subset.pop()
        backtrack(i + 1, subset)

    subset = []
    ans = []
    backtrack(0, subset)
    return ans


def subsets_2_bit(nums: list[int]) -> list[list[int]]:
    """
    Time: O(n * 2^n)
    Auxiliary Space: O(n)
    Output Space: O(n * 2^n)
    """
    n = len(nums)
    ans = []
    for i in range(1 << n):
        s = []
        for j in range(n):
            if i & (1 << j):
                s.append(nums[j])
        ans.append(s)
    return ans
