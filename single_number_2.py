class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for x in nums:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        for a,b in dict.items():
            if b == 1:
                return a