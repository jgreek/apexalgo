class GenerateParentheses:

    def __init__(self, n):
        self.n = n
        self.result = []

    def backtrack(self, current, openCount, closeCount, depth):
        """Helper recursive function to generate valid parentheses."""
        if len(current) == 2 * self.n:
            self.result.append(current)
            return

        if openCount < self.n:
            self.backtrack(current + '(', openCount + 1, closeCount, depth + 1)

        if closeCount < openCount:
            self.backtrack(current + ')', openCount, closeCount + 1, depth + 1)

    def generate(self):
        """Main function to initiate backtracking."""
        self.backtrack('', 0, 0, 0)
        return self.result


# Test Cases
def test():
    # Test Case 1
    generator = GenerateParentheses(3)
    result = generator.generate()
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert set(result) == set(expected), f"Expected {expected}, but got {result}"
    print(f"Test Case 1 Passed!")

    # Test Case 2
    generator = GenerateParentheses(1)
    result = generator.generate()
    expected = ["()"]
    assert set(result) == set(expected), f"Expected {expected}, but got {result}"
    print(f"Test Case 2 Passed!")

    # Test Case 3
    generator = GenerateParentheses(2)
    result = generator.generate()
    expected = ["(())", "()()"]
    assert set(result) == set(expected), f"Expected {expected}, but got {result}"
    print(f"Test Case 3 Passed!")


test()
