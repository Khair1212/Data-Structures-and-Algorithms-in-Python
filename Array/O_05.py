# Title: Largest Number At Least Twice of Others

class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums)< 1:
            return -1
        m = max(nums)
        for i in range(len(nums)):
            if i == nums.index(m):
                continue
            if 2*nums[i] > m:
                return -1
        return nums.index(m)