# Title: Check If N and Its Double Exist

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            if arr[i] * 2 in arr[i + 1:]:
                return True
            if arr[i] % 2 == 0 and arr[i] / 2 in arr[i + 1:]:
                return True
        return False
