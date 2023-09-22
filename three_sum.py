class Solution(object):
    def threeSum(self, nums):
        """
        This function finds all unique triplets in the array 'nums' which gives the sum of zero.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  # List to store the results
        nums.sort()  # Sort the numbers for efficient two pointer approach

        # Iterate through each number in the array
        for i, a in enumerate(nums):
            # Skip the same number to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1  # Two pointers
            while l < r:
                threeSum = a + nums[l] + nums[r]  # Calculate the current sum
                # If sum is greater than 0, move the right pointer to the left
                if threeSum > 0:
                    r -= 1
                # If sum is less than 0, move the left pointer to the right
                elif threeSum < 0:
                    l += 1
                else:  # Found a triplet
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Avoid duplicate triplets by skipping same numbers
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


# Test cases
solution = Solution()
assert sorted(solution.threeSum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
assert sorted(solution.threeSum([0, 0, 0])) == [[0, 0, 0]]
assert sorted(solution.threeSum([1, 2, -2, -1])) == []

print("All test cases passed!")
