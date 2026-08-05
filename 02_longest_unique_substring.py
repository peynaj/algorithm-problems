"""
Longest Substring Without Repeating Characters (The Longest Unique Substring)

Solutions:
1. basic (brute force)
2. sliding window
3. last index of characters

Space Complexity:
ASCII      -> O(128) => O(1)
Unicode    -> O(min(n, charset_size))
General CS -> O(n)
"""


def longest_unique_substring_1_basic(s: str) -> int:
    """
    check all substrings
    Time: O(n^2)
    Space: O(1)
    """
    result = 0
    n = len(s)
    for start in range(n):
        end = start
        seen = set()
        while end < n:
            ch = s[end]
            if ch in seen:
                break

            seen.add(ch)
            result = max(result, end-start+1)
            end += 1

    return result


def longest_unique_substring_2_sliding_window(s: str) -> int:
    """
    two pointer (left and right) for current window (initialized 0)
    a hash map for visited characters
    while right character is visited, unseen left character and move left pointer to right
    save see state of right character, update the longest length and move right pointer to right

    Time: O(n)
    Space: O(1)
    """
    result = 0
    left, right = 0, 0
    seen = set()
    while right < len(s):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        result = max(result, right - left + 1)
        right += 1

    return result


def longest_unique_substring_3_last_seen_index(s: str) -> int:
    """
    two pointer: start and end with 0 initialize
    hash map for save last index of any character in iterate all them
    if end character is visited, update start pointer to after last vist index of it

    Time: O(n)
    Space: O(1)
    """
    result = 0
    start = 0
    last_index = {}
    for end, end_ch in enumerate(s):
        if end_ch in last_index:
            # max -> do not move start backward
            start = max(start, last_index[end_ch] + 1)

        last_index[end_ch] = end
        result = max(result, end - start + 1)

    return result


def run_test():
    implementations = [
        longest_unique_substring_1_basic,
        longest_unique_substring_2_sliding_window,
        longest_unique_substring_3_last_seen_index,
    ]

    test_cases = [
        # string, expected_result
        ("a", 1),
        ("ab", 2),
        ("abba", 2),
        ("pwwkew", 3),
        ("abcabcbb", 3),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        ("abcdefabcbb", 6),
        ("aaa", 1),
        ("", 0),
        ("anviaj", 5),
        (" ", 1),
    ]

    for string, expected_result in test_cases:
        for func in implementations:
            result = func(string)
            assert result == expected_result, (
                F"Failed: {func.__name__} | {string=},{expected_result=},{result=}"
            )

    print("Tests finished.")


if __name__ == "__main__":
    run_test()
