class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        return "\u001F".join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        return s.split("\u001F")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

def test_codec():
    codec = Codec()

    # Test Case 1: Basic Strings
    strs1 = ["Hello", "World"]
    assert codec.decode(codec.encode(strs1)) == strs1, "Test Case 1 Failed"

    # Test Case 2: Strings with special characters
    strs2 = ["Hello|World", "123!@#"]
    assert codec.decode(codec.encode(strs2)) == strs2, "Test Case 2 Failed"

    # Test Case 3: Empty Strings
    strs3 = ["", "Hello"]
    assert codec.decode(codec.encode(strs3)) == strs3, "Test Case 3 Failed"

    # Test Case 4: Strings with spaces
    strs4 = ["Hello World", "Foo Bar"]
    assert codec.decode(codec.encode(strs4)) == strs4, "Test Case 4 Failed"

    # Test Case 5: Single String
    strs5 = ["HelloWorld"]
    assert codec.decode(codec.encode(strs5)) == strs5, "Test Case 5 Failed"

    print("All test cases passed!")


# Run the tests
test_codec()
