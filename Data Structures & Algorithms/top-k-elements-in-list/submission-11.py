class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = {}
        for i in nums:
            p[i] = 1 + p.get(i, 0)

        heap = []
        for num in p.keys():
            heapq.heappush(heap, (p[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]
