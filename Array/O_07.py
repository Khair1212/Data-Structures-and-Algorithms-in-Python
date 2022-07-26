class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) == len(set(nums))):
            return False
        return True

#         nums = sorted(nums)
#         print(nums)

#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False
