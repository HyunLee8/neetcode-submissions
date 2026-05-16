class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setA = set(nums)

        return len(set(nums)) != len(nums)
