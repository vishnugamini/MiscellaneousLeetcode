class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maxs = 1
        for x in range(len(s)):
            t = s[x]
            dic = {s[x] : 1}
            for y in range(x + 1,len(s)):
                if s[y] in dic:
                    break
                else:
                    dic[s[y]] = 1
                    t = t + s[y]
                maxs = max(maxs,len(t))
        return maxs


        