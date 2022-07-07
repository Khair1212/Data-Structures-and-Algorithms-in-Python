# Title: Array Partition I
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        summ = 0
        for i in range(0, len(nums), 2):
            mini = min(nums[i], nums[i + 1])
            summ += mini

        return summ
