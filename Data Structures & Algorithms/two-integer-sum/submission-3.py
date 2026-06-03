class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = dict()

        for each_i in range(len(nums)):
            
            if (target - nums[each_i]) in s:
                return [s[target - nums[each_i]], each_i]

            else:
                s[nums[each_i]] = each_i
            
        