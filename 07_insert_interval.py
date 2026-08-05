"""
Given a set of non-overlapping intervals[][]
 where intervals[i] = [starti , endi] represent the start and the end of the ith event
 and intervals is sorted in ascending order by starti and a new interval,
 insert the interval at the correct position such that after insertion,
 the intervals remain sorted.
If the insertion results in overlapping intervals, then merge the overlapping intervals.
Assume that the set of non-overlapping intervals is sorted based on start time.

Examples:

Input: intervals[][] = [[1, 3], [4, 5], [6, 7], [8, 10]], newInterval[] = [5, 6]
Output: [[1, 3], [4, 7], [8, 10]]
Explanation: The intervals [4, 5] and [6, 7] are overlapping with [5, 6].
 So, they are merged into one interval [4, 7].

Input: intervals[][] = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval[]  = [4, 9]
Output: [[1, 2], [3, 10], [12, 16]]
Explanation: The intervals [ [3, 5], [6, 7], [8, 10] ] are overlapping with [4, 9].
 So, they are merged into one interval [3, 10].
"""


def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    linear scan
    Time: O(n)
    Space: O(n)
    """
    if not intervals:
        return [new_interval]

    i = 0
    n = len(intervals)
    result = []
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        curr = intervals[i]
        new_interval[0] = min(new_interval[0], curr[0])
        new_interval[1] = max(new_interval[1], curr[1])
        i += 1

    result.append(new_interval)
    result.extend(intervals[i:])

    return result


test_cases = [
    [[[1, 3], [4, 5], [6, 7], [8, 10]], [5, 6]],
    [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9]],
    [[[1, 5]], [6, 8]],
    [[[1, 5]], [0, 3]],
    [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]],
    [[[5, 7]], [1, 3]],
    [[[1, 3]], [6, 8]],
    [[[2, 3], [5, 7], [9, 10]], [1, 12]],
    [[[1, 10]], [3, 5]],
]

for index, test in enumerate(test_cases):
    print(index, test)
    print(insert_interval(*test))
    print("-" * 80)
