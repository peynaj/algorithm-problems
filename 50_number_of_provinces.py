"""
There are n cities.
Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
 then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where
 isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
  and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        BFS
        Time: O(n ^ 2) ->
            Adjacency List: O(V+E)
            Visited Set: O(V)
            DFS Recursion Stack: O(V)
            E = n * (n-1) / 2 = O(n ^ 2)
        Space: O(n)
        """
        n = len(isConnected)

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in range(n):
                if isConnected[node][neighbour] == 1 and neighbour not in visited:
                    dfs(neighbour)

        for i in range(n):
            if i in visited:
                continue
            count += 1
            dfs(i)

        return count


def test():
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected = 2
    actual = Solution().findCircleNum(isConnected)
    assert expected == actual, print(f"{actual=} {expected=}")
    print("OK!")


if __name__ == "__main__":
    test()
