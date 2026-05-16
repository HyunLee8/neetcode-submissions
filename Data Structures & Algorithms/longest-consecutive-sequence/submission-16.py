class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        longest = 0

        for i in numSet:
            length = 1
            
            if i - 1 not in numSet:
                while (i + length) in numSet:
                    length += 1
            
                longest = max(length, longest)
                length = 1
        
        return longest


