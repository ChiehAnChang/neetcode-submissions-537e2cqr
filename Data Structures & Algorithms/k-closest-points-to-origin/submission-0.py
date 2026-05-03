from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            distance = self.distance(point)

            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (distance, point))
            elif distance < max_heap[0][0]:
                heapq.heapreplace_max(max_heap, (distance, point))

        return [point for distance, point in max_heap]

    def distance(self, point):
        x, y = point
        return x * x + y * y