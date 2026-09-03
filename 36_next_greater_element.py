"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
 element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""


def next_greater_element_1_two_loop(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Time: O(n * m)
    Space: O(1)
    """
    ans = []
    for x in nums1:
        find_self, find_greater = False, False
        i = 0
        while i < len(nums2) and not find_greater:
            y = nums2[i]
            if not find_self:
                if y == x:
                    find_self = True
            else:
                if y > x:
                    ans.append(y)
                    find_greater = True
                    break
            i += 1

        if not find_greater:
            ans.append(-1)
    return ans


def next_greater_element_2_monotonic_stack(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    next_greater = {}
    stack = []
    n = len(nums2)
    for i in range(n - 1, -1, -1):
        x = nums2[i]
        while stack and stack[-1] <= x:
            stack.pop()
        if stack:
            next_greater[x] = stack[-1]
        stack.append(x)

    ans = [next_greater.get(x, -1) for x in nums1]
    return ans


def run_tests():
    solutions = [
        next_greater_element_1_two_loop,
        next_greater_element_2_monotonic_stack,
    ]
    tests = [
        # nums1, nums2, expected
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
    ]

    for func in solutions:
        print(func.__name__, "...")
        for nums1, nums2, expected in tests:
            result = func(nums1, nums2)
            assert result == expected, f"{nums1=} {nums2=} --> {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
