class StairClimbing:
    """
    This class provides a solution for the stair climbing problem,
    where a person can climb either 1 or 2 steps at a time.
    """

    def climb_stairs(self, n: int) -> int:
        """
        Recursively computes the number of ways to climb a staircase of 'n' steps.

        Parameters:
        - n: int - Total steps in the staircase.

        Returns:
        - int: Number of distinct ways to climb the staircase.
        """
        # Base Case: if n is 0, it means we've found a valid way to climb the stairs
        if n == 0:
            return 1
        # Base Case: if n is negative, it means we've taken too many steps and it's not a valid way
        if n < 0:
            return 0

        # Recursively try taking 1 step and 2 steps, then sum the results
        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)


class Fibonacci:
    """
    This class calculates the Fibonacci number of a given index 'n'.
    """

    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        """
        Computes the Fibonacci number of index 'n' using memoization.

        Parameters:
        - n: int - The index for which the Fibonacci number is computed.

        Returns:
        - int: The Fibonacci number of index 'n'.
        """
        # Base cases for Fibonacci sequence
        if n == 0:
            return 0
        if n == 1:
            return 1

        # If the result is already in our memo dictionary, return that instead of recalculating
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]


# Test Cases
def test_solutions():
    stairs = StairClimbing()
    fibo = Fibonacci()

    # Stair Climbing Test Cases
    assert stairs.climb_stairs(2) == 2
    assert stairs.climb_stairs(3) == 3

    # Fibonacci Test Cases
    assert fibo.fib(0) == 0
    assert fibo.fib(1) == 1
    assert fibo.fib(2) == 1
    assert fibo.fib(3) == 2
    assert fibo.fib(4) == 3

    print("All test cases passed!")


if __name__ == "__main__":
    test_solutions()
