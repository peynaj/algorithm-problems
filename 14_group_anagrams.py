"""
Given an array arr[] of strings, group all anagrams together.
 Two strings are anagrams if they contain the same characters with the same frequencies,
 possibly in a different order.

Return a 2D array, where each inner array contains a group of anagrams.
The relative order of strings within each group should be the same as their order in arr.

Example:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]

Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]

---

[Naive Approach] Compare Every Pair of Strings - O(n^2 × m log m) Time and O(n+k) Space
[Better Approach] Using sorted words as keys - O(n*k*log(k)) Time and O(n*k) Space
[Expected Approach] Using Frequency as keys - O(n*k) Time and O(n*k) Space
"""


def group_anagrams_1_brute_force(strs: list[str]) -> list[list[str]]:
    """
    k = string max length
    Time: O(n^2 × k log k)
    Space: O(n + k)
    """
    if not strs:
        return []
    visited = set()
    res = []
    for i, word1 in enumerate(strs):
        if i in visited:
            continue
        visited.add(i)
        group = [word1]
        sorted_word1 = sorted(word1)
        for j in range(i + 1, len(strs)):
            word2 = strs[j]
            if j not in visited and sorted(word2) == sorted_word1:
                visited.add(j)
                group.append(word2)

        res.append(group)
    return res


def group_anagrams_2_sorted_word_as_cache_key(strs: list[str]) -> list[list[str]]:
    """
    k = strings max length
    Time: O(n * k * log(k))
    Space: O(n * k)
    """
    words_by_sorted_word = {}
    for word in strs:
        key = word.lower()
        key = "".join(sorted(key))
        if key not in words_by_sorted_word:
            words_by_sorted_word[key] = []
        words_by_sorted_word[key].append(word)

    return list(words_by_sorted_word.values())


def group_anagrams_3_frequency_as_cache_key(strs: list[str]) -> list[list[str]]:
    """
    Time: O(n * k)
    Space: O(n)
    """
    words_by_frequency = {}
    for word in strs:
        key = word.lower()
        frequency = [0] * 26
        for ch in key:
            frequency[ord(ch) - 97] += 1
        frequency = tuple(frequency)
        if frequency not in words_by_frequency:
            words_by_frequency[frequency] = []
        words_by_frequency[frequency].append(word)

    return list(words_by_frequency.values())


def run_tests():
    for test_case in [
        ["act", "god", "cat", "dog", "tac"],
        ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"],
    ]:
        print(f"{test_case=}")
        for solution in [
            group_anagrams_1_brute_force,
            group_anagrams_2_sorted_word_as_cache_key,
            group_anagrams_3_frequency_as_cache_key,
        ]:
            print(solution.__name__, ">")
            print(solution(test_case))
        print("-" * 80)
    print("Done!")


if __name__ == "__main__":
    run_tests()
