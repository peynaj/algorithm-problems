"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
 return the area of the largest rectangle in the histogram.
"""


def largest_rectangle_area_1_two_loop(heights: list[int]) -> int:
    """
    Time: O(n ^ 2)
    Space: O(1)
    """
    ans = 0
    n = len(heights)
    for i in range(n):
        min_height = heights[i]
        ans = max(ans, min_height)
        for j in range(i + 1, n):
            min_height = min(min_height, heights[j])
            ans = max(ans, min_height * (j - i + 1))

    return ans


def largest_rectangle_area_2_two_monotonic_stack(heights: list[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    n = len(heights)

    next_smaller = [n] * n
    st = []
    for i in range(n):
        while st and heights[i] < heights[st[-1]]:
            next_smaller[st.pop()] = i
        st.append(i)

    prev_smaller = [-1] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and heights[i] < heights[st[-1]]:
            prev_smaller[st.pop()] = i
        st.append(i)

    ans = 0
    for i in range(n):
        height = heights[i]
        width = next_smaller[i] - prev_smaller[i] - 1
        ans = max(ans, height * width)

    return ans


def largest_rectangle_area_3_single_stack(heights: list[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    heights.append(0)
    n = len(heights)
    st = []
    ans = 0
    for i in range(n):
        while st and heights[i] <= heights[st[-1]]:
            top = st.pop()
            width = (i - st[-1] - 1) if st else i
            area = heights[top] * width
            ans = max(ans, area)
        st.append(i)
    return ans


def run_tests():
    solutions = [
        largest_rectangle_area_1_two_loop,
        largest_rectangle_area_2_two_monotonic_stack,
        largest_rectangle_area_3_single_stack,
    ]
    tests = [
        # heights, expected
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([60, 20, 50, 40, 10, 50, 60], 100),
        ([3, 5, 1, 7, 5, 9], 15),
    ]
    for func in solutions:
        print(func.__name__, "...")
        for heights, expected in tests:
            result = func(heights)
            assert result == expected, f"{heights=} => {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
