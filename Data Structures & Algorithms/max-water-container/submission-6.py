class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res_max = 0
        left, right = 0, len(heights) - 1

        while left < right:
            left_height, right_height = heights[left], heights[right]
            curr_area = min(left_height, right_height) * (right - left)
            res_max = max(res_max, curr_area)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return res_max
