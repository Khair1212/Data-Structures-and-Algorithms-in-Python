# Title:  Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        arr = []
        hash_a = [0] * (l + 1)
        for i in range(l):
            hash_a[nums[i]] += 1
        for i in range(1, l + 1):
            if hash_a[i] == 0:
                arr.append(i)

        return arr