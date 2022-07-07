# Title: Spiral Matrix
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        ans = []

        while matrix:

            ans.extend(matrix.pop(0))  # left to right
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())  # top to bottom
            if matrix:
                ans.extend(matrix.pop()[::-1])  # right to left
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))  # bottom to top
        return ans


