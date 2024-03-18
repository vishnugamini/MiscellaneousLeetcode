class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        a = nums[n] * nums[n - 1] * nums[n - 2]
        b = nums[0] * nums[1] * nums[n]
        return max(a,b)
                