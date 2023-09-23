def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    cache = {}
    [cache.setdefault(tuple(sorted(s)), []).append(s) for s in strs]
    return list(cache.values())


# Test cases
def deep_sort(lst):
    return sorted([sorted(sublist) for sublist in lst])


# Test case 1: Basic test with multiple anagrams.
strs1 = ["eat", "tea", "tan", "ant", "bat"]
expected1 = [["eat", "tea"], ["tan", "ant"], ["bat"]]
result1 = groupAnagrams(strs1)
assert deep_sort(result1) == deep_sort(expected1)

# Test case 2: Empty string and single-character strings.
strs2 = ["", "a", "b", "a", ""]
expected2 = [["", ""], ["a", "a"], ["b"]]
result2 = groupAnagrams(strs2)
assert sorted(map(sorted, result2)) == sorted(expected2)

# Test case 3: No anagrams.
strs3 = ["hello", "world", "python"]
expected3 = [["hello"], ["world"], ["python"]]
result3 = groupAnagrams(strs3)
assert sorted(map(sorted, result3)) == sorted(expected3)

# Test case 4: Empty list.
strs4 = []
expected4 = []
result4 = groupAnagrams(strs4)
assert result4 == expected4

# Test case 5: All strings are anagrams of each other.
strs5 = ["abc", "bac", "cab"]
expected5 = [["abc", "bac", "cab"]]
result5 = groupAnagrams(strs5)
assert sorted(map(sorted, result5)) == sorted(expected5)

print("All test cases passed!")
