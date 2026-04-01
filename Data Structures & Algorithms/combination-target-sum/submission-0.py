class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        
        # Sorting is optional but helps with pruning
        candidates.sort() 

        def dfs(start_index, current_sum):
            
            # --- Base Cases ---
            
            # 1. Success Base Case
            if current_sum == target:
                res.append(subset.copy())
                return
            
            # 2. Failure Base Case (Pruning)
            if current_sum > target:
                return

            # --- Recursive Step (Choose / Explore / Unchoose) ---
            
            for i in range(start_index, len(candidates)):
                num = candidates[i]
                
                # --- This is the "Choose, Explore, Unchoose" trio ---
                
                # 1. Choose
                subset.append(num)
                
                # 2. Explore
                # CRITICAL: We pass 'i', not 'i + 1'.
                # This is what allows us to reuse the same number.
                dfs(i, current_sum + num)
                
                # 3. Unchoose (Backtrack)
                subset.pop()
                
        # Start from index 0 with a sum of 0
        dfs(0, 0)
        return res