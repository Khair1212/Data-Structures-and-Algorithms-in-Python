# Title: Longest Common Prefix
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(strs, key=len)
        if len(min_len) == 0:
            return ''

        for i in range(len(min_len), -1, -1):
            count = 0
            for j in range(len(strs)):
                if min_len[0:i] == strs[j][0:i]:
                    count += 1
            if count == len(strs):
                return min_len[0:i]

        return ''



