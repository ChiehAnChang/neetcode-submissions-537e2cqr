class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_list = set()
        for each_num in nums:
            if each_num in check_list:
                return True
            check_list.add(each_num)
        return False
        