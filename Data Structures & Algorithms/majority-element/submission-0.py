class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        required = int(len(nums)/2)

        d = dict()

        for each_num in nums:
            
            if each_num not in d:
                d[each_num] = 1
            else:
                d[each_num] += 1
            
            if d[each_num] > required:
                return each_num
        