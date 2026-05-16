class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        totalw = 0
        maxh = min(height[l], height[r]) #initialize the max heights

        while l < r:
            if height[l] > height[r]:
                r -= 1
                if maxh - height[r] >= 0:
                    totalw += maxh - height[r] #ts mf was a l not a r 
                else:
                    maxh = min(height[l], height[r])
            else:
                l += 1
                if maxh - height[l] >= 0:
                    totalw += maxh - height[l]
                else:
                    maxh = min(height[l], height[r])
        
        return totalw
            