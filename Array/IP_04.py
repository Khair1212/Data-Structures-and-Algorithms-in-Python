# Title: Sort Array by Parity

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = []
        for i in range(len(nums)):
            if (nums[i]) % 2 == 0:
                nums2.insert(0, nums[i])
            else:
                nums2.append(nums[i])
        return nums2
