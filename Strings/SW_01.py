# Title: Minimum Size Subarray Problem

# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/277445/Python-Sliding-Window-Approach-(with-comments)
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = 9999999
        s = 0
        i = 0
        for j in range(len(nums)):
            s += nums[j]
            while (s >= target):
                res = min(res, j - i + 1)
                s -= nums[i]
                i = i + 1

        return res if res <= len(nums) else 0




