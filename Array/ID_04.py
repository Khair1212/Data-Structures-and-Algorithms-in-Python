# Title:  Duplicate Zeros
# Link: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/


class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = arr.copy()
        j = 0
        size = len(arr)
        for i in range(len(arr2)):
            if (arr2[i] == 0):
                arr.insert(j+1,  0)
                arr.pop()
                j+=1
            j+=1