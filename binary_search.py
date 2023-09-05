from typing import List


class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        """
        Implements the Binary Search algorithm to find the target in the sorted list nums.

        Parameters:
        - nums: List[int] - A sorted list of integers.
        - target: int - The target integer to search for in the list.

        Returns:
        - int: The index of the target if found, or -1 if the target is not in the list.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Test cases
def test_binary_search():
    bs = BinarySearch()

    # Test Case 1: Target is present in the list
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    assert bs.search(nums1, target1) == 4

    # Test Case 2: Target is not present in the list
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    assert bs.search(nums2, target2) == -1

    # Test Case 3: Empty list
    nums3 = []
    target3 = 0
    assert bs.search(nums3, target3) == -1

    # Test Case 4: Target is the only element in the list
    nums4 = [5]
    target4 = 5
    assert bs.search(nums4, target4) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_binary_search()
