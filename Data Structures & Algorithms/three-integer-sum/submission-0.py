class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for each_num_i in range(n):
            # 跳過重複的第一個數
            if each_num_i > 0 and nums[each_num_i] == nums[each_num_i - 1]:
                continue

            target = -nums[each_num_i]
            left_i, right_j = each_num_i + 1, n - 1

            while left_i < right_j:
                s = nums[left_i] + nums[right_j]

                if s < target:
                    left_i += 1
                elif s > target:
                    right_j -= 1
                else:
                    # 三個數字本身（不是 target）
                    res.append([nums[each_num_i], nums[left_i], nums[right_j]])

                    # 先移動指標
                    left_i += 1
                    right_j -= 1

                    # 跳過左邊重複
                    while left_i < right_j and nums[left_i] == nums[left_i - 1]:
                        left_i += 1
                    # 跳過右邊重複（這時候 right_j+1 一定在範圍內）
                    while left_i < right_j and nums[right_j] == nums[right_j + 1]:
                        right_j -= 1

        return res
