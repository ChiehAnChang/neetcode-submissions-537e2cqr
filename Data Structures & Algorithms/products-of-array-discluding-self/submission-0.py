class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_list = []
        post_list = [0] * len(nums)

        res = [0] * len(nums)

        # prefix: pre_list[i] = nums[0] * ... * nums[i]
        for each_num_i in range(len(nums)):
            each_num = nums[each_num_i]
            if each_num_i != 0:
                pre_list.append(pre_list[each_num_i - 1] * each_num)
            else:
                pre_list.append(each_num)
        
        # postfix: post_list[i] = nums[i] * ... * nums[n-1]
        for each_num_i in range(len(nums) - 1, -1, -1):
            each_num = nums[each_num_i]
            if each_num_i != (len(nums) - 1):
                post_list[each_num_i] = post_list[each_num_i + 1] * each_num
            else:
                post_list[each_num_i] = each_num

        # build result: product except self
        for i in range(len(nums)):
            if i == 0:
                res[i] = post_list[i + 1]
            elif i == (len(nums) - 1):      # fix: len(num) -> len(nums)
                res[i] = pre_list[i - 1]
            else:
                res[i] = pre_list[i - 1] * post_list[i + 1]
        
        return res
