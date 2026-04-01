class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_list = {}
        for i in range(len(nums)):
            number = nums[i]
            diff = target - number
            if number in check_list:
                return [check_list[number], i]
            else:
                check_list[diff] = i
        return []