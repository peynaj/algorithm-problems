"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
 where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


def exist(board: list[list[str]], word: str) -> bool:
    """
    DFS + Backtrack
    Time: O(R * C * 4 ^ L)
    Space: O(L)
    """
    rows = len(board)
    cols = len(board[0])

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    visited = set()

    def backtrack(r, c, i):
        # visited item / out of board / wrong character
        if (r, c) in visited or i >= len(word) or r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        if i == len(word) - 1:
            return True

        visited.add((r, c))
        for dr, dc in directions:
            if backtrack(r + dr, c + dc, i + 1):
                return True

        visited.remove((r, c))
        return False

    for x in range(rows):
        for y in range(cols):
            if backtrack(x, y, 0):
                return True
    return False


def run_tests():
    test_cases = [
        # board, word, excepted
        ([["A", "B", "C", "D"]], "ABCD", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
    ]
    for board, word, excepted in test_cases:
        result = exist(board, word)
        assert result == excepted, f"{board=} {word=} -> {excepted=} {result=}"

    print("Done.")


if __name__ == "__main__":
    run_tests()
