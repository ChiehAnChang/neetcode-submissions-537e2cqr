class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        storage = set()
        
        for each_n in nums:
            storage.add(each_n)

        res_max = 1
        for each_n in nums:

            if each_n - 1 not in storage:
                # this is the begining
                curr_max = 1
                curr_n = each_n
                while curr_n + 1 in storage:
                    curr_max += 1
                    curr_n += 1
                res_max = max(curr_max, res_max)
            
        
        return res_max