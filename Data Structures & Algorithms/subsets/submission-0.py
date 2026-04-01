class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start_index, subset):
            # Add the current subset (a copy) at every step
            res.append(subset.copy())

            # Loop through all possible "next" elements
            for i in range(start_index, len(nums)):
                
                # 1. Make the choice
                subset.append(nums[i])
                
                # 2. Recurse, starting from the *next* index
                dfs(i + 1, subset)
                
                # 3. Undo the choice (backtrack)
                subset.pop()

        # Start with index 0 and an empty subset
        dfs(0, [])
        return res