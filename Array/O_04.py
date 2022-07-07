# Title: Find Pivot Index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum = 0
        rsum = 0

        for i in range(0, len(nums)):
            lsum = sum(nums[:i])
            rsum = sum(nums[i + 1:len(nums)])
            if lsum == rsum:
                return i
        return -1
