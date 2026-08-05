"""
Given two arrays start[] and end[]
 such that start[i] is the starting time of ith meeting
 and end[i] is the ending time of ith meeting.
 Return the minimum number of rooms required to attend all meetings.

Note: A person can also attend a meeting if it's starting time is same as the previous meeting's ending time.

Examples:

Input: start[] = [1, 10, 7], end[] = [4, 15, 10]
Output: 1
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings in a single room.

Input: start[] = [2, 9, 6], end[] = [4, 12, 10]
Output: 2
Explanation: 1st and 2nd meetings at one room but for 3rd meeting one another room required.

https://www.geeksforgeeks.org/dsa/meeting-rooms-find-minimum-meeting-rooms/
"""


def meeting_room_2_solution_1_brut_force(start: list[int], end: list[int]) -> int:
    """
    Time: O(n ^ 2)
    Space: O(1)
    """
    res = 1
    n = len(start)

    for i in range(n):
        room = 1
        for j in range(n):
            if i != j and start[j] <= start[i] < end[j]:
                room += 1

        res = max(res, room)

    return res


def meeting_room_2_solution_2_sort(start: list[int], end: list[int]) -> int:
    """
    Time: O(n log n)
    Space: O(1)
    """
    res = 0
    current_rooms = 0
    n = len(start)
    start.sort()
    end.sort()

    i, j = 0, 0
    while i < n:
        if start[i] < end[j]:
            current_rooms += 1
            i += 1
        else:
            current_rooms -= 1
            j += 1
        res = max(res, current_rooms)

    return res


def meeting_room_2_solution_3_prefix_sum(start: list[int], end: list[int]) -> int:
    """
    Time: O(n + max(end))
    Space: O(n)
    """
    res = 1
    n = len(start)
    meet_count = {}
    max_end = end[0]
    for i in range(n):
        s, e = start[i], end[i]
        meet_count[s] = meet_count.get(s, 0) + 1
        meet_count[e] = meet_count.get(e, 0) - 1
        max_end = max(max_end, e)

    room = 0
    for i in range(max_end + 1):
        room += meet_count.get(i, 0)
        res = max(res, room)

    return res

# ========================== Test =====================


solutions = [
    meeting_room_2_solution_1_brut_force,
    meeting_room_2_solution_2_sort,
    meeting_room_2_solution_3_prefix_sum,
]

test_cases = [
    [[1, 10, 7], [4, 15, 10]],
    [[2, 9, 6], [4, 12, 10]],
]

for index, test_input in enumerate(test_cases):
    print(index, *test_input)
    for func in solutions:
        print(func.__name__)
        print(func(*test_input))
        print("-" * 80)
