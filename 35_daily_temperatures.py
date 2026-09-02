"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such
 that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
 If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""


def daily_temperatures_1_brute_force(temperatures: list[int]) -> list[int]:
    """
    Time: O(n ^ 2)
    Space: O(n)
    """
    ans = []
    n = len(temperatures)
    for i in range(n):
        j = i + 1
        while j < n:
            if temperatures[j] > temperatures[i]:
                ans.append(j - i)
                break
            else:
                j += 1
        if j == n:
            ans.append(0)
    return ans


def daily_temperatures_2_stack(temperatures: list[int]) -> list[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_i = stack.pop()
            ans[prev_i] = i - prev_i

        stack.append(i)
    return ans


def run_tests():
    solutions = [
        daily_temperatures_1_brute_force,
        daily_temperatures_2_stack,
    ]
    tests = [
        # temperatures, expected
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ]
    for func in solutions:
        print(func.__name__, "...")
        for temperatures, expected in tests:
            result = func(temperatures)
            assert result == expected, f"{temperatures=} --> {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
