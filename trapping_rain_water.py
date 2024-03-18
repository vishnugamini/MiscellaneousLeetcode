class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1
        left_max = 0
        right_max = 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    result += (left_max - height[l])
                l += 1
            
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    result += (right_max - height[r])
                r -= 1
        return result
    