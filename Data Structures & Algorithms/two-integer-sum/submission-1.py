class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check_list = dict()

        for each_num_i in range(len(nums)):
            each_num = nums[each_num_i]
            complement = target - each_num
            if complement in check_list:
                return [check_list[complement], each_num_i]
            else:
                check_list[each_num] = each_num_i
    