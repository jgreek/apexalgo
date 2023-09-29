from collections import deque


class MinStack:

    def __init__(self):
        # Main stack to store all values
        self.stack = deque()

        # Additional stack to store minimum values at each state of the main stack
        self.min_stack = deque()

    def push(self, val: int) -> None:
        """Push a value onto the main stack.
        If the value is less than or equal to the current minimum, push it onto the min_stack.
        """
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Remove and return the top value from the main stack.
        If the top value is equal to the current minimum, pop it from the min_stack as well.
        """
        if self.stack:
            if self.min_stack[-1] == self.stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        return None

    def top(self) -> int:
        """Return the top value from the main stack without removing it."""
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """Return the current minimum value in the stack."""
        return self.min_stack[-1] if self.min_stack else None


# Test cases

# 1. Basic push/pop/top/getMin operations
min_stack = MinStack()
min_stack.push(3)
min_stack.push(1)
min_stack.push(4)
assert min_stack.getMin() == 1
assert min_stack.top() == 4
min_stack.pop()
assert min_stack.getMin() == 1
min_stack.pop()
assert min_stack.getMin() == 3

# 2. Handle empty stack gracefully
empty_stack = MinStack()
assert empty_stack.top() == None
assert empty_stack.getMin() == None
empty_stack.pop()  # this should not throw an error

# 3. Handling duplicates and multiple minimums
dup_stack = MinStack()
dup_stack.push(2)
dup_stack.push(2)
assert dup_stack.getMin() == 2
dup_stack.pop()
assert dup_stack.getMin() == 2
dup_stack.push(1)
assert dup_stack.getMin() == 1
dup_stack.pop()
assert dup_stack.getMin() == 2
print("All test cases pass")