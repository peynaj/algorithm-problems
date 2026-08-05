"""
Two Sum Problem

Given an array of n integers and a target value,
return a pair of indices whose sum equals the target.

Solutions:
1. Brute Force
2. Sort + Binary Search
3. Sort + Two Pointer
4. Hash Map

Approach                    Time        Space
------------------------------------------------
Brute Force                 O(n²)       O(1)
Sort + Binary Search        O(n log n)  O(n)
Sort + Two Pointer          O(n log n)  O(n)
Hash Map                    O(n)        O(n)

"""
from typing import Optional


def two_sum_1_brute_force(arr: list[int], target: int) -> Optional[tuple[int, int]]:
    """
    Basic solution by brute force and nested iteration to check all pairs of items
    Time: O(n^2)
    Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return i, j


def two_sum_2_sort_and_binary_search(arr: list[int], target: int) -> Optional[tuple[int, int]]:
    """
    step 1: Sort arr
    step 2: Check complement of each item by binary search
    Time: O(n log n)
    Space: O(n)
    """

    def _binary_search(pair_arr, start, target):
        left, right = start, len(pair_arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if pair_arr[mid][0] == target:
                return pair_arr[mid]
            elif pair_arr[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return

    indices_arr = [(num, i) for i, num in enumerate(arr)]
    indices_arr = sorted(indices_arr, key=lambda item: item[0])
    for i, pair in enumerate(indices_arr):
        num, num_index = pair
        complement = target - num
        found_complement = _binary_search(indices_arr, i+1, complement)
        if found_complement is not None:
            return num_index, found_complement[1]


def two_sum_3_sort_and_check_with_two_pointer(
        arr: list[int], target: int
) -> Optional[tuple[int, int]]:
    """
    step 1: sort arr
    step 2: check complement with Two-Pointer technique
    Time: O(n log n)
    Space: O(n)
    """
    indices_arr = [(num, i) for i, num in enumerate(arr)]
    indices_arr = sorted(indices_arr, key=lambda item: item[0])
    left, right = 0, len(arr) - 1
    while left < right:
        left_item, right_item = indices_arr[left], indices_arr[right]
        current_sum = left_item[0] + right_item[0]
        if current_sum == target:
            return left_item[1], right_item[1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1


def two_sum_4_hash_map(arr: list[int], target: int) -> Optional[tuple[int, int]]:
    """
    step 1: a has map for save index of items
    step 2: iterate items and check complement exist in hash map
    Time: O(n)
    Space: O(n)
    """
    seen = {}
    for num_index, num in enumerate(arr):
        complement = target - num
        complement_index = seen.get(complement)
        if complement_index is not None:
            return num_index, complement_index
        seen[num] = num_index


# ========================= Tests ================================

def run_tests():
    test_cases = [
        # arr, target, has_solution
        ([0, -1, 2, -3, 1], -2, True),
        ([1, -2, 1, 0, 5], 0, False),
        ([3, 3], 6, True),
        ([3, 2, 4], 6, True),
        ([], 5, False),
        ([1], 1, False),
    ]

    implementations = [
        two_sum_1_brute_force,
        two_sum_2_sort_and_binary_search,
        two_sum_3_sort_and_check_with_two_pointer,
        two_sum_4_hash_map,
    ]

    def assert_valid_result(arr, target, result, has_solution):
        if not has_solution:
            assert result is None
            return

        assert result is not None

        i, j = result
        assert i != j
        assert 0 <= i < len(arr)
        assert 0 <= j < len(arr)
        assert arr[i] + arr[j] == target

    for func in implementations:
        for arr, target, has_solution in test_cases:
            result = func(arr, target)
            try:
                assert_valid_result(arr, target, result, has_solution)
            except AssertionError:
                print(f"Failed: Algorithm: {func.__name__} | "
                      f"Test Case: {arr=} {target=} {has_solution=}")
                raise

    print("Tests finished.")


if __name__ == "__main__":
    run_tests()
