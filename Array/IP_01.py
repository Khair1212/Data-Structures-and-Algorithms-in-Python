# Title: Replace Elements with Greatest Element on Right Side

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 0:
            return arr
        for i in range(len(arr)-1):
            maxima = max(arr[i+1:])
            arr[i] = maxima
        arr[len(arr)-1] = -1
        return arr