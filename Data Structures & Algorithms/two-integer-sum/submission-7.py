class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}
        for i in range(len(nums)):
            if target - nums[i] in p:
                return [p[target - nums[i]], i]
            else:
                p[nums[i]] = i