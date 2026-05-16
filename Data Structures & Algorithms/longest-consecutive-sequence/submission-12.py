class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = sorted(set(nums))
        print(s)
        count = 1
        maxx = 1
        for i in range(len(s) - 1):
            if s[i + 1] == s[i] + 1:
                count += 1
            else:
                if count > maxx:
                    maxx = count
                count = 1
        
        return max(count, maxx)

