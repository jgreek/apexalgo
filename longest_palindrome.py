from collections import Counter


class PalindromeBuilder:

    @staticmethod
    def longest_palindrome_length(s: str) -> int:
        ans = 0  # Initialize the answer to 0

        # Create a counter for the string s to count occurrences of each character
        # Then iterate over the count values
        for v in Counter(s).values():
            # Add to ans the largest even number less than or equal to v
            ans += v // 2 * 2

            # Check if the current total length of palindrome is even and the character count is odd
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1  # Use one of these characters as the middle character of the palindrome

        # Return the total length of the longest possible palindrome
        return ans


# Test cases
if __name__ == "__main__":
    builder = PalindromeBuilder()

    # Test Case 1
    s1 = "abccccdd"
    expected_output1 = 7  # dccaccd
    assert builder.longest_palindrome_length(s1) == expected_output1

    # Test Case 2
    s2 = "aabb"
    expected_output2 = 4  # abba
    assert builder.longest_palindrome_length(s2) == expected_output2

    # Test Case 3
    s3 = "abcdefg"
    expected_output3 = 1  # a (or any other single letter from s)
    assert builder.longest_palindrome_length(s3) == expected_output3

    print("All test cases passed!")
