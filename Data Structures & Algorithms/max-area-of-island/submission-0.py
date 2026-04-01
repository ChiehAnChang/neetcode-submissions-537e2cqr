from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])

        # [FIX 1] WAS: -float(inf)
        # REASON: If the grid has no islands (all 0s), the result should be 0, not negative infinity.
        curr_max = 0 
        
        for each_row in range(n_rows):
            for each_col in range(n_cols):
                curr_cell = grid[each_row][each_col]

                # [FIX 2] WAS: if curr_cell == "1":
                # REASON: The input grid contains Integers (1), not Strings ("1").
                if curr_cell == 1:
                    
                    # [FIX 3] WAS: (Missing this line)
                    # REASON: You must mark the starting cell as "V" immediately so you don't visit it again.
                    grid[each_row][each_col] = "V"
                    
                    area = self.bfs(grid, (each_row, each_col), n_rows, n_cols)
                    curr_max = max(curr_max, area)
        return curr_max
        
    def bfs(self, grid, cell_infos, total_rows, total_cols):
        area = 1
        
        # [FIX 4] WAS: q = deque(cell_infos)
        # REASON: deque((0,0)) creates deque([0, 0]). You need a list inside: deque([(0,0)]).
        q = deque([cell_infos])

        while q:
            curr_row, curr_col = q.popleft()
            
            choices = [(curr_row + 1, curr_col), 
                       (curr_row - 1, curr_col), 
                       (curr_row, curr_col + 1), 
                       (curr_row, curr_col - 1)]
            
            for each_choice in choices:
                r, c = each_choice[0], each_choice[1]
                
                # [FIX 5] WAS: ... and grid[...][...] == "1": if grid... == "V": area += 1
                # REASON: You had the logic backwards. You look for LAND (1), then turn it into "V".
                # If you check for "V" here, you are looking for spots you already visited!
                if (0 <= r <= total_rows - 1) and \
                   (0 <= c <= total_cols - 1) and \
                   grid[r][c] == 1:
                    
                    # [FIX 6] Mark as "V" immediately!
                    # This stops the infinite loop.
                    grid[r][c] = "V"
                    area += 1
                    q.append(each_choice)

        return area