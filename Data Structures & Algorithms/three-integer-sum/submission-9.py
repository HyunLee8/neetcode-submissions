class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums) - 1):
            l, r =  i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if nums[i] + s > 0:
                    r -=  1
                elif nums[i] + s < 0:
                    l += 1
                else:
                    res.add(tuple(sorted([nums[r], nums[l], nums[i]])))
                    r -= 1
                    l += 1
        
        return [list(t) for t in res]