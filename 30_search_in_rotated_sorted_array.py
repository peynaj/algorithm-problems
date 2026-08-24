"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
 such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
 return the index of target if it is in nums, or -1 if it is not in nums.
"""


def search_in_rotated_sorted_arrays_1_linear_search(nums: list[int], target: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1


def search_in_rotated_sorted_arrays_2_twice_binary_search(nums: list[int], target: int) -> int:
    """
    Time: O(log n)
    Space: O(1)
    """
    n = len(nums)

    # find pivot
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            # right is not sorted
            low = mid + 1
        else:
            # left is not sorted
            high = mid
    pivot = low

    # binary search
    if nums[pivot] == target:
        return pivot

    if pivot == 0:
        low, high = 0, n - 1
    elif nums[0] <= target:
        low, high = 0, pivot - 1
    else:
        low, high = pivot + 1, n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def search_in_rotated_sorted_arrays_3_single_binary_search(nums: list[int], target: int) -> int:
    """
    Time: O(log n)
    Space: O(1)
    """
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        # left is sorted
        if nums[mid] >= nums[low]:
            # target in left sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # right is sorted
        else:
            # target in right sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def tests():
    solutions = [
        search_in_rotated_sorted_arrays_1_linear_search,
        search_in_rotated_sorted_arrays_2_twice_binary_search,
        search_in_rotated_sorted_arrays_3_single_binary_search,
    ]
    test_cases = [
        # nums, target, expected
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], 2, 9),
        ([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], 11, -1),
        ([3, 1], 3, 0),
        ([1, 2, 3, 4, 5], 3, 2),
        ([2, 1], 1, 1),
        ([5, 1, 2, 3, 4], 5, 0),
    ]

    for func in solutions:
        print(func.__name__, "...")
        for (nums, target, expected) in test_cases:
            result = func(nums, target)
            assert result == expected, f"{nums=} {target=} ===> {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    tests()
