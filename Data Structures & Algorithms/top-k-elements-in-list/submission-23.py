class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = {}
        for num in nums:
            p[num] = 1 + p.get(num, 0)
        
        heap = []
        for num, cnt in p.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for cnt, num in heap]