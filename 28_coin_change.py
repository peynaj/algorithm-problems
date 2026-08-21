"""
You are given an integer array coins representing coins of different denominations
 and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
 If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


def coin_change_1_recursion(coins: list[int], target: int) -> int:
    """
    Time: O(n ** target)
    Space: O(target)
    """

    max_number = float("inf")

    def coin_min_recursive(i, coins, target):
        if target == 0:
            return 0
        if target < 0 or i == len(coins):
            return max_number

        include_i = 1 + coin_min_recursive(i, coins, target - coins[i])
        exclude_i = coin_min_recursive(i + 1, coins, target)
        return min(include_i, exclude_i)

    ans = coin_min_recursive(0, coins, target)
    return ans if ans != max_number else -1


def coin_change_2_top_down_memoization(coins: list[int], target: int) -> int:
    """
    Time: O(n * target)
    Space: O(n * target)
    """

    max_number = float("inf")

    def coin_min_recursive(i, target, coins, memo):
        if target == 0:
            return 0
        if target < 0 or i == len(coins):
            return max_number

        if memo[i][target] != -1:
            return memo[i][target]

        include_i = 1 + coin_min_recursive(i, target - coins[i], coins, memo)
        exclude_i = coin_min_recursive(i + 1, target, coins, memo)
        memo[i][target] = min(include_i, exclude_i)
        return memo[i][target]

    memo = [[-1] * (target + 1) for _ in range(len(coins))]
    ans = coin_min_recursive(0, target, coins, memo)
    return ans if ans != max_number else -1


def coin_change_3_bottom_up_tabulation(coins: list[int], target: int) -> int:
    """
    Time: O(n * target)
    Space: O(n * target)
    """

    max_number = float("inf")
    n = len(coins)
    dp = [[0] * (target + 1) for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(1, target + 1):
            dp[i][j] = max_number
            include_i = max_number
            exclude_i = max_number

            if j - coins[i] >= 0:
                include_i = 1 + dp[i][j - coins[i]]

            if i + 1 < n:
                exclude_i = dp[i + 1][j]

            dp[i][j] = min(include_i, exclude_i)

    ans = dp[0][target]
    return ans if ans != max_number else -1


def coin_change_4_space_optimized_dp(coins: list[int], target: int) -> int:
    """
    Time: O(n * target)
    Space: O(target)
    """

    max_number = float("inf")
    n = len(coins)
    dp = [max_number] * (target + 1)
    dp[0] = 0

    for i in range(n - 1, -1, -1):
        for j in range(1, target + 1):
            include_i = max_number
            exclude_i = max_number

            if j - coins[i] >= 0:
                include_i = 1 + dp[j - coins[i]]

            if i + 1 < n:
                exclude_i = dp[j]

            dp[j] = min(include_i, exclude_i)

    ans = dp[target]
    return ans if ans != max_number else -1


def run_tests():
    solutions = [
        coin_change_1_recursion,
        coin_change_2_top_down_memoization,
        coin_change_3_bottom_up_tabulation,
        coin_change_4_space_optimized_dp,
    ]
    test_cases = [
        # coins, target, expected
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]
    for func in solutions:
        print(func.__name__, "...")
        for i, (coins, target, expected) in enumerate(test_cases):
            print(f"> Test {i}")
            result = func(coins, target)
            assert result == expected, f"{i=} {coins=} {target=} ===> {expected=} {result=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
