# Title: Valid Mountain Array

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        maximum = max(arr)
        ind = arr.index(maximum)

        if maximum == arr[0] or maximum == arr[-1]:
            return False

        for i in range(len(arr)):
            if (len(arr)) < 3:
                return False
            if (i == ind):
                continue
            if i < ind and (arr[i] >= arr[i + 1]):
                return False
            elif i > ind and (arr[i] >= arr[i - 1]):
                return False
        return True
