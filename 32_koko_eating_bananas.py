"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
 The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
 and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
 and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""


def min_eating_speed_1_linear_search(piles: list[int], h: int) -> int:
    """
    Time: O(m * n) (m: max of piles, n: number of piles)
    Space: O(1)
    """
    mx = max(piles)
    ans = mx
    for speed in range(1, mx + 1):
        req_time = 0
        for x in piles:
            req_time += x // speed + (1 if x % speed else 0)
        if req_time <= h and speed < ans:
            ans = speed
    return ans


def min_eating_speed_2_binary_search_on_answer(piles: list[int], h: int) -> int:
    """
    Time: O(n * log m) (m: max of piles, n: number of piles)
    Space: O(1)
    """
    mx = max(piles)
    lo, hi = 1, mx
    ans = mx
    while lo <= hi:
        speed = (lo + hi) // 2
        req_time = 0
        for x in piles:
            req_time += (x + speed - 1) // speed
            if req_time > h:
                break

        if req_time > h:
            lo = speed + 1
        else:
            hi = speed - 1
            ans = min(ans, speed)
    return ans


def run_tests():
    solutions = [
        min_eating_speed_1_linear_search,
        min_eating_speed_2_binary_search_on_answer,
    ]
    test_cases = [
        # piles, h, expected
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ]
    for func in solutions:
        print(func.__name__, "...")
        for piles, h, expected in test_cases:
            result = func(piles, h)
            assert result == expected, f"{piles=} {h=} ===> {result=} {expected=}"

    print("Done!")


if __name__ == "__main__":
    run_tests()
