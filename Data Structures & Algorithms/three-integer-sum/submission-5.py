class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for target_i in range(len(nums)):
            # Skip duplicate target numbers
            if target_i > 0 and nums[target_i] == nums[target_i - 1]:
                continue

            target = nums[target_i]
            check_set = set()

            for potential_i in range(target_i + 1, len(nums)):
                curr_num = nums[potential_i]
                needed_num = -target - curr_num

                if needed_num in check_set:
                    res.add((target, needed_num, curr_num))

                check_set.add(curr_num)

        return [list(triplet) for triplet in res]