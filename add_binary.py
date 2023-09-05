class BinaryAddition:
    def add_binary_v1(self, a: str, b: str) -> str:
        """
        This method adds two binary strings and returns their sum as a binary string.
        It manually handles the binary addition without relying on built-in Python methods.
        """

        result = []
        carry = 0
        for i in range(max(len(a), len(b))):
            num_a = int(a[-i - 1]) if i < len(a) else 0
            num_b = int(b[-i - 1]) if i < len(b) else 0

            curr_sum = num_a + num_b + carry

            if curr_sum > 1:
                curr_sum %= 2
                carry = 1
            else:
                carry = 0

            result.append(curr_sum)

        if carry:
            result.append(1)

        return "".join(map(str, result[::-1]))

    def add_binary_v2(self, a: str, b: str) -> str:
        """
        This method adds two binary strings using built-in Python functions
        to convert between binary and integer representations.
        """

        # Convert binary strings to integers using int function
        int_a = int(a, 2)
        int_b = int(b, 2)

        # Convert the sum back to binary using bin function
        return bin(int_a + int_b)[2:]


def test_binary_addition():
    binary_addition = BinaryAddition()

    # Test Case 1
    a1, b1 = "11", "1"
    expected_output1 = "100"
    assert binary_addition.add_binary_v1(a1, b1) == expected_output1
    assert binary_addition.add_binary_v2(a1, b1) == expected_output1

    # Test Case 2
    a2, b2 = "1010", "1011"
    expected_output2 = "10101"
    assert binary_addition.add_binary_v1(a2, b2) == expected_output2
    assert binary_addition.add_binary_v2(a2, b2) == expected_output2

    print("All test cases passed!")


if __name__ == "__main__":
    test_binary_addition()