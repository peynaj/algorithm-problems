"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected,
 and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
 return the maximum amount of money you can rob tonight without alerting the police.
"""


def rob_1_brute_force(nums: list[int]) -> int:
    """
    Time: O(2 ^ n)
    Space: O(n)
    """
    n = len(nums)

    def helper(index: int) -> int:
        if index == 0:
            return nums[0]
        if index == 1:
            return max(nums[0], nums[1])
        include_this = nums[index] + helper(index - 2)
        exclude_this = helper(index - 1)
        return max(include_this, exclude_this)

    return helper(n - 1)


def rob_2_top_down_memoization(nums: list[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    n = len(nums)
    memo = {0: nums[0], 1: max(nums[:2])}

    def helper(index: int) -> int:
        if index in memo:
            return memo[index]
        include_this = nums[index] + helper(index - 2)
        exclude_this = helper(index - 1)
        memo[index] = max(include_this, exclude_this)
        return memo[index]

    return helper(n - 1)


def rob_3_bottom_up_tabulation(nums: list[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[:2])

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[:2])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]


def rob_4_bottom_up_space_optimized(nums: list[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    perv = nums[0]
    curr = max(nums[:2])

    for i in range(2, len(nums)):
        perv, curr = curr, max(nums[i] + perv, curr)

    return curr


def run_tests():
    solutions = [
        rob_1_brute_force,
        rob_2_top_down_memoization,
        rob_3_bottom_up_tabulation,
        rob_4_bottom_up_space_optimized,
    ]
    test_cases = [
        # nums, expected
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([114, 117, 207, 117, 235, 82, 90, 67, 143, 146, 53, 108, 200, 91, 80, 223, 58, 170, 110, 236, 81, 90, 222, 160,
          165, 195, 187, 199, 114, 235, 197, 187, 69, 129, 64, 214, 228, 78, 188, 67, 205, 94, 205, 169, 241, 202, 144,
          240], 4173),
    ]
    for func in solutions:
        print(f"Start to test solution: {func.__name__} ...")
        for i, (nums, expected) in enumerate(test_cases):
            if "brute_force" in func.__name__ and i == 2:
                continue

            actual = func(nums)
            try:
                assert actual == expected
            except AssertionError:
                print(f"[!] Failed > {nums=}, {expected=}, {actual=}")
                raise
        print("OK!")


if __name__ == "__main__":
    run_tests()
