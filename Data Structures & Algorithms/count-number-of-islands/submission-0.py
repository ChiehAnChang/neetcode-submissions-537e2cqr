class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        n_rows, n_cols = len(grid), len(grid[0])
        island = 0

        for each_row in range(n_rows):
            for each_col in range(n_cols):
                
                # BUG FIX 1: Only start BFS if it is LAND ('1'). 
                # Ignore water ('0') and already visited ('V').
                if grid[each_row][each_col] == '1':
                    island += 1
                    
                    # BUG FIX 2: Correct deque initialization with a list inside
                    q = deque([(each_row, each_col)])
                    
                    # Mark start node as visited immediately so we don't process it again
                    grid[each_row][each_col] = "V" 

                    while q:
                        new_row, new_col = q.popleft()
                        
                        # Define directions (Up, Down, Left, Right)
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        
                        for dr, dc in directions:
                            curr_row, curr_col = new_row + dr, new_col + dc

                            # BUG FIX 3: Check bounds on the NEIGHBOR (curr), not the parent (new)
                            if 0 <= curr_row < n_rows and 0 <= curr_col < n_cols:
                                # BUG FIX 4: Only add to queue if it is LAND ('1')
                                if grid[curr_row][curr_col] == '1':
                                    q.append((curr_row, curr_col))
                                    # CRITICAL: Mark as visited immediately to prevent infinite loop
                                    grid[curr_row][curr_col] = "V"
        return island