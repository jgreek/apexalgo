from collections import Counter


class AnagramChecker:

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Test cases
if __name__ == "__main__":
    checker = AnagramChecker()

    # Test Case 1: Simple anagrams
    s1, t1 = "listen", "silent"
    assert checker.is_anagram(s1, t1) == True

    # Test Case 2: Different lengths
    s2, t2 = "hello", "helloo"
    assert checker.is_anagram(s2, t2) == False

    # Test Case 3: Different characters
    s3, t3 = "apple", "appla"
    assert checker.is_anagram(s3, t3) == False

    # Test Case 4: Same string
    s4, t4 = "banana", "banana"
    assert checker.is_anagram(s4, t4) == True

    # Test Case 5: Empty strings
    s5, t5 = "", ""
    assert checker.is_anagram(s5, t5) == True

    print("All test cases passed!")
