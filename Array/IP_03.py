# Title: Move Zeros

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if (nums[j] == 0):
                nums.pop(j)
                nums.append(0)
                j -= 1
            j += 1

