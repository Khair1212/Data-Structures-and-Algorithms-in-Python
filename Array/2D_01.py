# Title: Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}

        # loop through matrix
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # if no entry in the dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                # if we've already passsed over this diagonal, keep adding elements to it!
                    d[i+j].append(mat[i][j])

        # We are done with the pass, let's build our answer array
        ans = []

        # look at the diagonal and each diagonal's elements

        for key, values in d.items():

            # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ..])
            # snake time, look at the diagonal level

            if (key%2 ==0):
                # here we append in reverse order because it's even numbered level/diagonal
                [ans.append(x) for x in values[::-1]]
            else:
                ans.extend(values)
        return ans


