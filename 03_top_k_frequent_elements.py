"""
Top K Frequent Elements
"""
import heapq


def top_k_frequent_elements_1_priority_queue(nums: list[int], k: int) -> list[int]:
    """
    Time: O(n log n)
        count by num: O(n)
        frequent max heap creation: O(m log m)  [m = unique items count, m < n]
        frequent max heap pop: O(k log m)
        Total: O(n) + O(m log m) + O(k log m) -> O(n log n)

    Space: O(n)
        count_by_num: O(n)
        frequent_max_heap: O(n)
        Total: O(2n) -> O(n)
    """
    count_by_num = {}
    for num in nums:
        if num not in count_by_num:
            count_by_num[num] = 0
        count_by_num[num] += 1
    frequent_heap = []
    for num, count in count_by_num.items():
        heapq.heappush(frequent_heap, (count, num))
        if len(frequent_heap) > k:
            heapq.heappop(frequent_heap)

    result = []
    while len(result) < k and frequent_heap:
        item = heapq.heappop(frequent_heap)
        result.append(item[1])
    result.reverse()
    return result


def run_test():
    implementations = [
        top_k_frequent_elements_1_priority_queue,
    ]
    test_cases = [
        # nums, k, expected_result
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([], 0, []),
        ([1], 1, [1]),
        ([1, 1, 1], 1, [1]),
        # ([1, 2, 3], 3, [1, 2, 3]),
    ]

    for func in implementations:
        for nums, k, expected_result in test_cases:
            result = func(nums, k)

            assert len(result) == len(expected_result), (
                f"Failed: {func.__name__}, {nums=}, {k=}, {len(result)}!={len(expected_result)}"
            )
            for i, num in enumerate(expected_result):
                assert num == result[i], (
                    f"Failed: {func.__name__}, {nums=}, {k=}, {expected_result=}, {result=}"
                )

    print("Tests finished.")


if __name__ == "__main__":
    run_test()
