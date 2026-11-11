"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""


def length_of_lis_1_basic(nums: list[int]) -> int:
    """
    Time: O(2 ^ n)
    Space: O(n)
    """
    n = len(nums)

    def helper(index: int) -> int:
        mx = 1
        for prev in range(index):
            if nums[prev] < nums[index]:
                mx = max(mx, helper(prev) + 1)
        return mx

    result = 1
    for i in range(1, n):
        result = max(result, helper(i))
    return result


def length_of_lis_2_memoization(nums: list[int]) -> int:
    """
    Time: O(n ^ 2)
    Space: O(n)
    """
    n = len(nums)
    memo = {0: 1}

    def helper(index: int) -> int:
        if index in memo:
            return memo[index]
        mx = 1
        for prev in range(index):
            if nums[prev] < nums[index]:
                mx = max(mx, helper(prev) + 1)
        memo[index] = mx
        return mx

    result = 1
    for i in range(1, n):
        result = max(result, helper(i))
    return result


def length_of_lis_3_tabulation(nums: list[int]) -> int:
    """
    Time: O(n ^ 2)
    Space: O(n)
    """
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for prev in range(i):
            if nums[prev] < nums[i]:
                dp[i] = max(dp[i], dp[prev] + 1)

    return max(dp)


def length_of_lis_4_binary_search(nums: list[int]) -> int:
    """
    Time: O(n log n)
    Space: O(n)
    """
    ans = [nums[0]]

    for x in nums[1:]:
        if x > ans[-1]:
            ans.append(x)
        else:
            left, right = 0, len(ans) - 1
            while left < right:
                mid = left + (right - left) // 2
                if ans[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            ans[left] = x

    return len(ans)


solutions = [
    length_of_lis_1_basic,
    length_of_lis_2_memoization,
    length_of_lis_3_tabulation,
    length_of_lis_4_binary_search,
]
test_cases = [
    # nums, expected
    ([3, 10, 2, 1, 20], 3),
    ([30, 20, 10], 1),
    ([2, 2, 2], 1),
    ([3, 4, 5, 1, 2, 3, 4], 4),
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
]


def run_tests():
    for func in solutions:
        print(f"Start to test {func.__name__} ...")
        for nums, expected in test_cases:
            actual = func(nums)
            try:
                assert actual == expected
            except AssertionError:
                print(f"[Failed] {nums=}, {expected=}, {actual=}")
                raise
        print("OK!")


if __name__ == "__main__":
    run_tests()
