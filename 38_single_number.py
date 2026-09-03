"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


def single_number_1_linear_search(nums: list[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    for x in nums:
        if x in seen:
            seen.remove(x)
        else:
            seen.add(x)
    return seen and seen.pop()


def single_number_2_xor(nums: list[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    ans = 0
    for x in nums:
        ans ^= x
    return ans


def run_tests():
    solutions = [
        single_number_1_linear_search,
        single_number_2_xor,
    ]
    tests = [
        # nums, expected
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ]
    for func in solutions:
        print(func.__name__, "...")
        for nums, expected in tests:
            result = func(nums)
            assert result == expected, f"{nums=} => {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
