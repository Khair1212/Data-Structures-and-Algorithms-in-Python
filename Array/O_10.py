class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in dic:
                dic[sorted_word].append(word)
            else:
                dic[sorted_word] = [word]

        results = []
        for item in dic.values():
            results.append(item)

        return results

#         res = defaultdict(list)

#         for s in strs:
#             count = [0] * 26 # a .. z

#             for c in s:
#                 count[ord(c)-ord('a')] +=1
#             res[tuple(count)].append(s)

#         return res.values()


