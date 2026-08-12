"""
Given an undirected graph g, the task is to print the number of connected components in the graph.
"""


class UndirectedGraph:

    def __init__(self, v: int):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, i, j):
        self.adj[i].append(j)
        self.adj[j].append(i)

    def number_of_connected_components(self) -> int:
        """
        Time: O(V+E)
        Space: O(V+E)
        Extra Space: O(h)
        """
        visited = [False for _ in range(self.v)]
        c = 0
        for i in range(self.v):
            if not visited[i]:
                self.dfs_util(i, visited)
                c += 1
        return c

    def dfs_util(self, i, visited):
        visited[i] = True
        for j in self.adj[i]:
            if not visited[j]:
                self.dfs_util(j, visited)


def run_tests():
    g = UndirectedGraph(5)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    ans1 = g.number_of_connected_components()
    assert ans1 == 2, f"{ans1=}"
    print("Done!")


if __name__ == "__main__":
    run_tests()
