class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s + nums[i] > 0:
                    r -= 1
                elif s + nums[i] < 0:
                    l += 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    r -= 1
                    l += 1
        
        res_list = []
        for i in res:
            res_list.append(i)
        return res_list