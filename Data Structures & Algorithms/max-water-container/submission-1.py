class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        curr_max = 0

        left_i, right_j = 0, len(heights) - 1

        while left_i < right_j:
            left = heights[left_i]
            right = heights[right_j]
            curr_max = max(curr_max, min(left, right) * (right_j - left_i))

            if left < right:
                left_i += 1      
            else:
                right_j -= 1

            
        return curr_max
