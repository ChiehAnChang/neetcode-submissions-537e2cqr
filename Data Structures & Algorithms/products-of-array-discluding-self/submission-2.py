from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # Fix 1: Range starts at 1 because prefix[0] is already 1 (base case)
        for each_prefix in range(1, len(nums)):
            # We multiply the previous accumulated product by the PREVIOUS number
            prefix[each_prefix] = prefix[each_prefix - 1] * nums[each_prefix - 1]
        
        # Fix 2: Range starts from second-to-last element down to 0
        for each_suffix in range(len(nums) - 2, -1, -1):
            # Fix 3: We multiply the next accumulated product by the NEXT number
            suffix[each_suffix] = suffix[each_suffix + 1] * nums[each_suffix + 1]
    
        # Optional: Print to debug
        # print(prefix)
        # print(suffix)

        res = [1] * len(nums)
        for each_i in range(len(prefix)):
            res[each_i] = prefix[each_i] * suffix[each_i]
        
        return res