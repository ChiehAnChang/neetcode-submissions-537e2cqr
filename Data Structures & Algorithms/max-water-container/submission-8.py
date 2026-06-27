class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        curr_max = 0

        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)
            curr_max = max(curr_max, curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return curr_max