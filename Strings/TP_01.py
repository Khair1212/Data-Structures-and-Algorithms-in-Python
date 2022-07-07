# Title: Revers String
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        for i in range(len(s)):
            if i == j or j < i:
                break
            if s[i] != s[j]:
                temp = s[j]
                s[j] = s[i]
                s[i] = temp
            j -= 1


