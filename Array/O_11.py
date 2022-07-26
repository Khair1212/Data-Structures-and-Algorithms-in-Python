class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

#         dic = {}
#         for num in nums:
#             dic[num] = 1 + dic.get(num, 0)


#         dic = sorted(dic.items(), key = lambda x:x[1],  reverse = True)
#         result = []

#         j = 0
#         for item in dic:
#             if j>=k:
#                 break
#             result.append(item[0])
#             j+=1
#         return result

