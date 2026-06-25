class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        number_set = set(nums)
        max_length = 0

        for each_num in nums:

            if each_num -1 not in number_set:

                curr_length = 1

                while each_num + curr_length in number_set:
                    curr_length += 1
                    
                
                max_length = max(max_length, curr_length)

        return max_length