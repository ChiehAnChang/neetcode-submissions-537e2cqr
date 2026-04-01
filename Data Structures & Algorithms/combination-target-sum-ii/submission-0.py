class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        candidates.sort()
        def dfs(path, curr_sum, target, start_index):

            if curr_sum == target:

                res.append(path.copy())


            for each_index in range(start_index, len(candidates)):

                each_choice = candidates[each_index]

                if each_index > start_index and candidates[each_index - 1] == candidates[each_index]:
                    continue

                if  curr_sum + each_choice > target:
                    continue

                path.append(each_choice)
                
                dfs(path, curr_sum + each_choice, target, each_index + 1)

                path.pop()

        dfs([], 0, target, 0)
        return res
