from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_Rows = len(grid)
        num_Cols = len(grid[0])

        dq = deque()

        # Step 1: 找出所有 treasure chest (0)，加進 queue
        for r in range(num_Rows):
            for c in range(num_Cols):
                if grid[r][c] == 0:
                    dq.append((r, c))

        # Step 2: 開始 BFS
        while dq:
            r, c = dq.popleft()

            directions = [
                [0, -1],
                [0, 1],
                [-1, 0],
                [1, 0]
            ]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                # 檢查邊界與是否為可走的土地
                if 0 <= new_r < num_Rows and 0 <= new_c < num_Cols and grid[new_r][new_c] != -1:
                    # 如果新的距離更短就更新
                    if grid[new_r][new_c] > grid[r][c] + 1:
                        grid[new_r][new_c] = grid[r][c] + 1
                        dq.append((new_r, new_c))
