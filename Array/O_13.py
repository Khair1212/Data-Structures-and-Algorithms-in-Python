class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longest = 0

        for n in nums:

            if (n - 1) not in nums:
                y = n + 1
                while y in nums:
                    y += 1
                longest = max(longest, y - n)

        return longest

