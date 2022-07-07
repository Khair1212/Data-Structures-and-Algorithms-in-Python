# Title: Remove element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        while True:
            if val in nums:
                count += 1
                nums.remove(val)
            else:
                break
