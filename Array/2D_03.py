# Title: Pascal's Triangle

# Simple adding the previous two value which is on [i-1][j-1] and [i-1][j] th location
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = []
        for i in range(numRows):
            li = []
            for j in range(i + 1):
                if j == 0 or j == i:  # if j is the first or last index then just append 1
                    li.append(1)
                else:
                    li.append(matrix[i - 1][j - 1] + matrix[i - 1][j])  # else add the previous two values
            matrix.append(li)

        return matrix
