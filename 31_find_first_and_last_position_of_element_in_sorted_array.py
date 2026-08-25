"""
Given an array of integers nums sorted in non-decreasing order,
 find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
"""


def search_range_1_linear_search(nums: list[int], target: int) -> list[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    pos1, pos2 = -1, -1
    for i in range(len(nums)):
        x = nums[i]
        if x == target:
            if pos1 == -1:
                pos1 = pos2 = i
            else:
                pos2 = i

    return [pos1, pos2]


def search_range_2_twice_binary_search(nums: list[int], target: int) -> list[int]:
    """
    Time: O(log n)
    Space: O(1)
    """
    if not nums:
        return [-1, -1]

    pos1, pos2 = -1, -1
    n = len(nums)
    # find first position
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if mid - 1 < 0 or nums[mid - 1] != target:
                pos1 = mid
                break
            else:
                hi = mid - 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    if pos1 == -1:
        return [-1, -1]

    # find last position
    lo, hi = pos1, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if mid + 1 >= n or nums[mid + 1] != target:
                pos2 = mid
                break
            else:
                lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    if pos2 == -1:
        pos2 = pos1

    return [pos1, pos2]


def run_tests():
    solutions = [
        search_range_1_linear_search,
        search_range_2_twice_binary_search,
    ]
    tests = [
        # nums, target, expected
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 1, [-1, -1]),
        ([5, 7, 7, 8, 8, 10], 5, [0, 0]),
        ([5, 7, 7, 8, 8, 10], 10, [5, 5]),
    ]
    for func in solutions:
        print(func.__name__, "...")
        for nums, target, expected in tests:
            result = func(nums, target)
            assert result == expected, f"{nums=} {target=} ===> {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
