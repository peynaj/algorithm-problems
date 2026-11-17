"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions
 in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""


class Solution:
    """
    Time: O(n log n)
    Space: O(n)
    """

    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_two_list(a: list[int], b: list[int]):
            ans = []
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    ans.append(a[i])
                    i += 1
                else:
                    ans.append(b[j])
                    j += 1

            while i < len(a):
                ans.append(a[i])
                i += 1
            while j < len(b):
                ans.append(b[j])
                j += 1
            return ans

        def merge_sort(arr, left, right):
            if left > right:
                return []
            if left == right:
                return [arr[left]]
            mid = (left + right) // 2
            l1 = merge_sort(arr, left, mid)
            l2 = merge_sort(arr, mid + 1, right)
            return merge_two_list(l1, l2)

        return merge_sort(nums, 0, len(nums) - 1)


def main():
    nums = [0, 5, 1, 10, 2, 0]
    print(f"{nums=}")
    sorted_nums = Solution().sortArray(nums)
    print(f"{sorted_nums=}")


if __name__ == "__main__":
    main()
