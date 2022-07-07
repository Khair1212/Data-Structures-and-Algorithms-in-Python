# Title: Max Consecutive Ones
# link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cons = 0
        max_cons = 0
        for num in nums:
            if num == 0:
                cons = 0
            else:
                cons += 1
                if cons > max_cons:
                    max_cons = cons
        return max_cons
