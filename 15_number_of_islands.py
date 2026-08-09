"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

4-direction connectivity
"""
from collections import deque
from pprint import pprint


def number_of_islands_1_dfs(grid: list[list[str]]) -> int:
    """
    Time: O(n * m)
    Space: O(n * m)
    """
    if not grid or not grid[0]:
        return 0

    land = "1"
    rows = len(grid)
    cols = len(grid[0])
    # 4-direction connectivity
    directions = [
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
    ]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_safe(r, c):
        return bool(0 <= r < rows and 0 <= c < cols and grid[r][c] == land and not visited[r][c])

    islands_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == land and not visited[r][c]:
                visited[r][c] = True
                islands_count += 1

                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if is_safe(nr, nc):
                            visited[nr][nc] = True
                            stack.append((nr, nc))

    return islands_count


def number_of_islands_2_bfs(grid: list[list[str]]) -> int:
    """
    Time: O(n * m)
    Space: O(n * m)
    """
    if not grid or not grid[0]:
        return 0

    land = "1"
    rows = len(grid)
    cols = len(grid[0])
    # 4-direction connectivity
    directions = [
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
    ]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_safe(r, c):
        return bool(0 <= r < rows and 0 <= c < cols and grid[r][c] == land and not visited[r][c])

    def bfs(start_r, start_c):
        q = deque()
        q.append((start_r, start_c))
        visited[start_r][start_c] = True
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_safe(nr, nc):
                    visited[nr][nc] = True
                    q.append((nr, nc))

    islands_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == land and not visited[i][j]:
                bfs(i, j)
                islands_count += 1

    return islands_count


def number_of_islands_3_disjoint_sets(grid: list[list[str]]) -> int:
    """
    Solution: disjoint sets
    Time: O(n * m)
    Space: O(n * m)
    """
    if not grid or not grid[0]:
        return 0

    land = "1"
    rows = len(grid)
    cols = len(grid[0])
    ds = DisjointUnionSets(rows * cols)

    # 4-direction connectivity
    directions = [
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
        # (-1, -1),
        # (-1, 1),
        # (1, -1),
        # (1, 1)
    ]

    # union set for all connected lands
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == land:
                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == land:
                        x = r * cols + c
                        y = next_r * cols + next_c
                        ds.union_sets(x, y)

    unique_islands = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == land:
                unique_islands.add(ds.find(r * cols + c))

    # print(ds.parent)
    # print(ds.rank)
    # print(unique_islands)

    return len(unique_islands)


class DisjointUnionSets:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, i):
        root = self.parent[i]
        # Path Compression
        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]
        return root

    def union_sets(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        # Union by Rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def run_test():
    input_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    output_1 = 1
    input_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    output_2 = 3
    input_3 = [
        ["0", "1", "0"],
        ["1", "0", "1"],
        ["0", "1", "0"]
    ]
    output_3 = 4
    test_case = [
        (input_1, output_1),
        (input_2, output_2),
        (input_3, output_3),
    ]

    solutions = [
        number_of_islands_1_dfs,
        number_of_islands_2_bfs,
        number_of_islands_3_disjoint_sets
    ]

    for index, (grid, expected) in enumerate(test_case):
        print(f"{index=}")
        pprint(grid)

        for func in solutions:
            print(func.__name__, ">")
            res = func(grid)
            print(f"{res=}")
            assert res == expected, f"{index=} {expected=} {res=}"

        print("-" * 80)

    print("Done!")


if __name__ == "__main__":
    run_test()
