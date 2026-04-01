class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        number_set = set()

        for each_num in nums:
            number_set.add(each_num)

        curr_longest = 0
        curr_length = 0
        for each_num in nums:
            if each_num - 1 not in number_set:
                curr_length = 1
                curr_num  = each_num
                while curr_num + 1 in number_set:
                    curr_length += 1
                    curr_num = curr_num + 1

                curr_longest = max(curr_length, curr_longest)

        return curr_longest
