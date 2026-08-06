"""
Binary Search is a searching algorithm that operates on a sorted or monotonic search space,
 repeatedly dividing it into halves to find a target value or optimal answer in logarithmic time O(log N).
"""


def binary_search(nums: list[int], target: int) -> int:
    """
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def run_test():
    for i, (nums, target, expected) in enumerate(
        [
            [[2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23, 5],
            [[1, 2, 3, 4, 5], 6, -1],
            [[1, 2, 3, 4, 5, 6], 3, 2],
            [[1, 2, 3, 4, 5, 6], 1, 0],
            [[1, 2, 3, 4, 5, 6], 6, 5],
            [[], 1, -1],
            [[1], 1, 0],
            [[1], 2, -1],
            [[1, 2], 1, 0]
        ]
    ):
        result = binary_search(nums, target)
        assert result == expected, f"{i=} {nums=} {target=} {expected=} {result=}"

    print("All tests passed!")


if __name__ == "__main__":
    run_test()
