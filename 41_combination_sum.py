"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique
 combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target
 is less than 150 combinations for the given input.
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    n = number of candidates
    T = target
    M = minimum of candidates

    Time: O(n ^ (T/M))
    Auxiliary Space: O(T/M)
    Output Space: O(n ^ (T/M))
    """
    ans = []

    def backtrack(i: int, combination: list[int], s: int):
        if i >= len(candidates):
            return
        if s == 0 and combination:
            ans.append(list(combination))
            return

        x = candidates[i]
        # include i
        if s >= x:
            combination.append(x)
            backtrack(i, combination, s - x)
            combination.pop()
        # exclude i
        backtrack(i + 1, combination, s)

    backtrack(0, [], target)
    return ans


def run_tests():
    for candidates, target in [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([1, 2, 3], 5),
        ([2], 1),
        ([2, 4], 1),
    ]:
        result = combination_sum(candidates, target)
        print(f"{candidates=} {target=}\n{result=}\n---")


if __name__ == "__main__":
    run_tests()
