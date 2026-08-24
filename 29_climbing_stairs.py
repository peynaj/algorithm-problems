"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs_1_recursion(n: int) -> int:
    """
    Time: O(2 ^ n)
    Space: O(1)
    """
    if n <= 2:
        return n
    return climb_stairs_1_recursion(n - 1) + climb_stairs_1_recursion(n - 2)


def climb_stairs_2_dp(n: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    dp = [1, 2]
    while len(dp) < n:
        dp.append(sum(dp[-2:]))
    return dp[n - 1]


def climb_stairs_3_space_optimized(n: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if n <= 2:
        return n
    prev1 = 1
    prev2 = 1
    for _ in range(n - 1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2


# TODO: Matrix Exponentiation – O(log n) Time and O(1) Space

def run_tests():
    solutions = [
        climb_stairs_1_recursion,
        climb_stairs_2_dp,
        climb_stairs_3_space_optimized,
    ]
    for func in solutions:
        print(func.__name__, "...")
        for (n, expected) in [
            (2, 2),
            (3, 3),
            (5, 8),
            (7, 21),
            (10, 89),
            (11, 144),
        ]:
            result = func(n)
            assert result == expected, f"{n=} ===> {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
