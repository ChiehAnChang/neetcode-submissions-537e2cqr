class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checklist = set()

        for each_num in nums:
            if each_num in checklist:
                return True
            else:
                checklist.add(each_num)
        return False