class Solution:

    def isPossible(self, S):
        x = {}
        c = 0
        for r in S:
            if r in x:
                x[r] += 1
            else:
                x[r] = 1
        for t in x.values():
            if t % 2 != 0:
                return "NO"
            elif t == 1:
                c += 1
        if  c <= 1:
            return "Yes"
        else:
            return "No"
