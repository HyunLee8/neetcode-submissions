class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = {}
        for i in nums:
            p[i] = 1 + p.get(i, 0)

        return heapq.nlargest(k, p, key=p.get)