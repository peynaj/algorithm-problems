"""
Course Schedule II

---

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""


class Solution:
    """
    Time: O(V+E)
    Space: O(V+E)
    """

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        order = []
        adj = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            adj[i].append(j)
        visited = [False] * numCourses
        rec_stack = [False] * numCourses

        def dfs(index):
            if rec_stack[index]:
                return False
            if visited[index]:
                return True

            visited[index] = True
            rec_stack[index] = True
            for a in adj[index]:
                if not dfs(a):
                    return False

            rec_stack[index] = False
            order.append(index)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order


def is_valid_order(order, num_courses, prerequisites):
    if len(order) != num_courses:
        return False

    if len(set(order)) != num_courses:
        return False

    position = {course: i for i, course in enumerate(order)}

    for course, prerequisite in prerequisites:
        if position[prerequisite] >= position[course]:
            return False

    return True


def run_tests():
    s = Solution()
    cases = [
        # numCourses, prerequisites, expected
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]),
        (1, [], [0]),
        (2, [[1, 0], [0, 1]], []),
        (1, [[0, 0]], []),
        (3, [[1, 0], [2, 1], [0, 2]], []),
        (2, [[1, 0], [1, 0]], [0, 1]),
    ]
    for numCourses, prerequisites, expected in cases:
        actual = s.findOrder(numCourses, prerequisites)
        if len(expected) == 0:
            if len(actual) != 0:
                raise AssertionError(f"{numCourses=} {prerequisites=} {expected=} {actual=}")
        else:
            assert is_valid_order(actual, numCourses, prerequisites), \
                f"{numCourses=} {prerequisites=} {expected=} {actual=}"

    print(f"Done! ({len(cases)} tests)")


if __name__ == "__main__":
    run_tests()
