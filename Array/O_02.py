# Title: Third Maximum Number

class Solution:
    def thirdMax(self, nums) -> int:

        s = frozenset(nums)
        if (len(s)) == 1:
            return max(nums)
        if (len(s)) == 2:
            return max(nums)

        s = sorted(s, reverse=True)
        return s[2]