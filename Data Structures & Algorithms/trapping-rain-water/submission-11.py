class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxH = min(height[l], height[r])
        total_w = 0

        while l < r:
            if height[l] > height[r]:
                r -= 1
                if height[r] > maxH:
                    maxH = min(height[r], height[l])
                else:
                    total_w += maxH - height[r]
            else:
                l += 1
                if height[l] > maxH:
                    maxH = min(height[r], height[l])                    
                else:
                    total_w += maxH - height[l]
               
        return total_w