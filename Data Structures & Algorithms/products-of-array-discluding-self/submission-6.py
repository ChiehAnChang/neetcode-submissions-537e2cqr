from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        # 1. Build the prefix array
        for each_n_i in range(len(nums)):
            if each_n_i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[each_n_i - 1] * nums[each_n_i - 1])

        # 2. Build the suffix array
        for each_n_i in range(len(nums) - 1, -1, -1):
            if each_n_i == (len(nums) - 1):
                suffix.append(1)
            else:
                # FIXED: Use suffix[-1] to get the running product
                suffix.append(suffix[-1] * nums[each_n_i + 1])

        res = []

        # 3. Multiply them together
        for each_i in range(len(nums)):
            res.append(prefix[each_i] * suffix[len(nums) - each_i - 1])

        return res