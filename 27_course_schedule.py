"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
 you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Detect Cycle in a Directed Graph

"""


def dfs(adj, i, visited, rec_stack):
    if rec_stack[i]:
        return True

    if visited[i]:
        return False

    visited[i] = True
    rec_stack[i] = True

    for j in adj[i]:
        if dfs(adj, j, visited, rec_stack):
            return True

    rec_stack[i] = False

    return False


def is_cyclic(v, edges):
    adj = [[] for _ in range(v)]
    for i, j in edges:
        adj[i].append(j)

    visited = [False] * v
    rec_stack = [False] * v

    for i in range(v):
        if not visited[i] and dfs(adj, i, visited, rec_stack):
            return True

    return False


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    DFS Traversal to detect cycle
    Time: O(V+E)
    Space: O(V+E)
    """
    return False if is_cyclic(num_courses, prerequisites) else True


def run_tests():
    print("Test 1")
    assert can_finish(2, [[1, 0]])
    print("Test 2")
    assert not can_finish(2, [[1, 0], [0, 1]])
    print("Test 3")
    assert not can_finish(3, [[1, 0], [0, 2], [2, 1]])

    print("Done!")


if __name__ == "__main__":
    run_tests()
