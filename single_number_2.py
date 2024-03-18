class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        for a,b in dic.items():
            if b == 1:
                return a
        