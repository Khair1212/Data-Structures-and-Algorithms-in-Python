# Title: Squares of a Sorted Array
# Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [num ** 2 for num in nums]
        print(nums)

        return nums
