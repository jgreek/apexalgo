class Solution(object):
    def twoSum(self, numbers, target):
        """
        This function takes a sorted list 'numbers' and an integer 'target'.
        It returns the 1-based indices of two numbers such that they add up to the target.

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize two pointers at the beginning and end of the array.
        left = 0
        right = len(numbers) - 1

        # Continue until the two pointers meet.
        while left < right:
            # Calculate the current sum.
            current_sum = numbers[left] + numbers[right]

            # If the current sum matches the target, return the indices.
            if current_sum == target:
                return [left + 1, right + 1]  # 1-based indices

            # If the current sum is less than the target, move the left pointer to the right.
            if current_sum < target:
                left += 1
                # If the current sum is greater than the target, move the right pointer to the left.
            else:
                right -= 1
        return None  # Return None if no pair sums to the target


# Test cases
solution = Solution()
assert solution.twoSum([1, 2, 3, 4, 6], 5) == [1, 4]  # because 1 + 4 = 5
assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]  # because 2 + 7 = 9
assert solution.twoSum([-1, 0, 2, 3], 2) == [1, 4]  # because -1 + 3 = 2

# Adding a test case where no such pair exists, should return None
assert solution.twoSum([1, 2, 3, 4], 10) is None  # because no pair sums to 10

print("All test cases passed!")
