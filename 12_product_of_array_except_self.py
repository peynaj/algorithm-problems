"""
Given an integer array nums, return an array answer such
 that answer[i] is equal to the product of all the elements of nums except nums[i]
"""


def product_except_self_1_brute_force(nums: list[int]) -> list[int]:
    """
    Time: O(n ^ 2)
    Space: O(n)
    """
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                answer[i] *= nums[j]

    return answer


def product_except_self_2_1_prefix_and_suffix_array(nums: list[int]) -> list[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    n = len(nums)
    prefix_products = [1] * n
    suffix_products = [1] * n

    for i in range(1, n):
        prefix_products[i] = nums[i - 1] * prefix_products[i - 1]

    for i in range(n - 2, -1, -1):
        suffix_products[i] = nums[i + 1] * suffix_products[i + 1]

    answer = []
    for i in range(n):
        answer.append(suffix_products[i] * prefix_products[i])

    return answer


def product_except_self_2_2_prefix_and_suffix_value(nums: list[int]) -> list[int]:
    """
    Time: O(n)
    Extra Space: O(1)
    Total Space: O(n)
    """
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


def product_except_self_3_total_product(nums: list[int]) -> list[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    product_except_zero = 1
    zero_count = 0
    zero_index = -1
    for i, n in enumerate(nums):
        if n == 0:
            zero_index = i
            zero_count += 1
            if zero_count > 1:
                return [0] * len(nums)
        else:
            product_except_zero *= n

    answer = [0] * len(nums)
    if zero_count == 0:
        for i in range(len(nums)):
            answer[i] = product_except_zero // nums[i]
    else:
        answer[zero_index] = product_except_zero

    return answer


def run_tests():
    for nums in [
        [1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [0, 1, 0, 2, 3, 4],
    ]:
        print(f"{nums=}")
        for solution in [
            product_except_self_1_brute_force,
            product_except_self_2_1_prefix_and_suffix_array,
            product_except_self_2_2_prefix_and_suffix_value,
            product_except_self_3_total_product,
        ]:
            print(solution.__name__, "->")
            print(solution(nums))

        print("-" * 80)

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
