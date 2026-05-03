class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for each_num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, each_num)
            elif min_heap[0] < each_num:
                heapq.heapreplace(min_heap, each_num)

        return min_heap[0]