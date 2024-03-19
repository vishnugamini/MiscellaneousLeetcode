class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        t = str(n)
        for y in t:
            if y == "1":
                count += 1
        return count
        