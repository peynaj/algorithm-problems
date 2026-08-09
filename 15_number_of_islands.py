"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""
from pprint import pprint


def number_of_islands(grid: list[list[str]]) -> int:
    """
    Solution: disjoint sets
    Time: O(n * m)
    Space: O(n * m)
    """
    land = "1"
    n = len(grid)
    m = len(grid[0])
    ds = DisjointUnionSets(n * m)

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
    for h in range(n):
        for v in range(m):
            if grid[h][v] == land:
                for dh, dv in directions:
                    next_h, next_v = h + dh, v + dv
                    if 0 <= next_h < n and 0 <= next_v < m and grid[next_h][next_v] == land:
                        x = h * m + v
                        y = next_h * m + next_v
                        ds.union_sets(x, y)

    unique_islands = set()
    for h in range(n):
        for v in range(m):
            if grid[h][v] == land:
                unique_islands.add(ds.find(h * m + v))

    print(ds.parent)
    print(ds.rank)
    print(unique_islands)

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

    for index, (grid, expected) in enumerate(test_case):
        print(f"{index=}")
        pprint(grid)
        res = number_of_islands(grid)
        print(f"{res=}")
        assert res == expected, f"{index=} {expected=} {res=}"
        print("-" * 80)

    print("Done!")


if __name__ == "__main__":
    run_test()
