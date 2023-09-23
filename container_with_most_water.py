class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize the result to 0
        res = 0

        # Start with the leftmost and rightmost positions
        left = 0
        right = len(height) - 1

        # Continue until the two pointers meet
        while left < right:
            # Calculate the area formed by the current pair of bars
            area = (right - left) * min(height[left], height[right])

            # Update the result if the current area is larger than the previously recorded one
            res = max(res, area)

            # Move the pointer pointing to the shorter bar inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the maximum area found
        return res


def test_maxArea():
    solution = Solution()

    # Test Case 1: General case with varying bar heights.
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # Test Case 2: All bars are of the same height.
    assert solution.maxArea([6, 6, 6, 6, 6, 6]) == 30

    # Test Case 3: Bars are in increasing order.
    assert solution.maxArea([1, 2, 3, 4, 5, 6]) == 9

    # Test Case 4: Bars are in decreasing order.
    assert solution.maxArea([6, 5, 4, 3, 2, 1]) == 9

    # Test Case 5: Only two bars.
    assert solution.maxArea([1, 6]) == 1

    # Test Case 6: Empty list.
    assert solution.maxArea([]) == 0

    print("All test cases pass")


test_maxArea()
