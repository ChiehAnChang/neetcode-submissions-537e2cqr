from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            sec_heaviest = heapq.heappop_max(stones)

            if heaviest != sec_heaviest:
                heapq.heappush_max(stones, heaviest - sec_heaviest)

        return stones[0] if stones else 0