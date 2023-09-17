class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        tops = Counter(nums).most_common(k)
        return [top[0] for top in tops]

# Test cases
solution = Solution()

# Test case 1: Basic functionality.
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
expected1 = [1, 2]
assert set(solution.topKFrequent(nums1, k1)) == set(expected1)

# Test case 2: All elements are unique.
nums2 = [4, 5, 6, 7]
k2 = 2
expected2 = [4, 5]  # Since all frequencies are the same, the first `k` elements will be returned.
assert set(solution.topKFrequent(nums2, k2)) == set(expected2)

# Test case 3: Larger k than unique numbers.
nums3 = [1, 2, 3]
k3 = 5
expected3 = [1, 2, 3]  # All elements will be returned.
assert set(solution.topKFrequent(nums3, k3)) == set(expected3)

# Test case 4: Single element.
nums4 = [1]
k4 = 1
expected4 = [1]
assert set(solution.topKFrequent(nums4, k4)) == set(expected4)

# Test case 5: All elements have the same frequency.
nums5 = [3, 3, 2, 2, 1, 1]
k5 = 2
expected5 = [3, 2]  # The first `k` elements in the original order will be returned.
assert set(solution.topKFrequent(nums5, k5)) == set(expected5)

print("All test cases passed!")
