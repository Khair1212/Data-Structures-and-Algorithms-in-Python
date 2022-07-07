# Title: Find Numbers with Even Number of Digits
# Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_count = 0
        for num in nums:
            x = num / 10
            count = 1
            while (x > 0):
                x = x / 10
                count = count + 1
            if count % 2 == 0:
                even_count += 1
        return even_count

