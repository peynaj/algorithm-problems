"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permute(nums: list[int]) -> list[list[int]]:
    """
    Time: O(n * n!)
    Auxiliary Space: O(n)
    Output Space: O(n * n!)
    """
    n = len(nums)
    selected = [False] * n
    ans = []

    def backtrack(p):
        if len(p) == n:
            ans.append(list(p))
            return
        for i in range(n):
            if selected[i]:
                continue

            p.append(nums[i])
            selected[i] = True
            backtrack(p)
            p.pop()
            selected[i] = False

    backtrack([])

    return ans


def run_tests():
    nums = [1, 2, 3]
    print(f"{nums=}")
    permutations = permute(nums)
    print(f"{permutations=}")


if __name__ == "__main__":
    run_tests()
