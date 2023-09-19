class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
def main():
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4  # Returns 4 because the sequence [1,2,3,4] is the longest
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([1,2,3,5,6,100,200]) == 3  # Returns 3 because [1,2,3] is the longest consecutive sequence
    print("All tests passed!")
main()