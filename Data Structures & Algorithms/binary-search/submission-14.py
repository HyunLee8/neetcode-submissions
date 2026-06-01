class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)//2
        for i in range(len(nums)):
            if m < -1 or m >= len(nums):
                break
            if nums[m] == target:
                return m
            elif nums[m] > target:
                m -= 1
            else:
                m += 1
        
        return -1
