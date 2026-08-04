"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
"""
from copy import deepcopy


def merge_intervals_1_brute_force(intervals: list[list[int]]) -> list[list[int]]:
    """
    check all pairs in nested loop and reset after any overlap
    O(n ** 3)
    """
    if not intervals:
        return []
    result = deepcopy(intervals)
    changed = True
    while changed:
        changed = False
        for i in range(len(result)-1):
            for j in range(i+1, len(result)):
                # print(i, j, len(result), result)
                start1, end1 = result[i]
                start2, end2 = result[j]
                if max(start1, start2) <= min(end1, end2):
                    # find overlap
                    result[i] = [min(start1, start2), max(end1, end2)]
                    result.pop(j)
                    changed = True
                    break

            if changed:
                break

    return result


def merge_intervals_2_sort(intervals: list[list[int]]) -> list[list[int]]:
    """
    sort + linear scan
    sort: O(n log n)
    find overlap: O(n)
    total: O(n log n)
    """
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last = merged[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])
    return merged

# ==================================================================================


intervals_input = [[13, 20], [1, 4], [2, 5], [7, 9], [3, 6], [8, 10], [12, 15], [20, 25]]
implementations = [
    merge_intervals_1_brute_force,
    merge_intervals_2_sort,
]
for func in implementations:
    print(func.__name__)
    print(func(intervals_input))
    print("-" * 50)

# Outputs:
# [[12, 25], [1, 6], [7, 10]]
# [[1, 6], [7, 10], [12, 25]]

