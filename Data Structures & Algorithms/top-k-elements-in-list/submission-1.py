class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for each_n in nums:
            if each_n not in d:
                d[each_n] = 1
            else:
                d[each_n] += 1
        
        h = []
        heapq.heapify_max(h)

        for each_k in d:
            heapq.heappush_max(h, (d[each_k], each_k))

        res = []
        for _ in range(k):
            res.append(heapq.heappop_max(h)[1])
        return res