class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        res = 0
        left_i, right_j = 0, len(height) - 1
        left_max, right_max = height[left_i], height[right_j]

        while left_i < right_j:
            if left_max <= right_max:
                left_i += 1
                left_max = max(left_max, height[left_i])
                res += left_max - height[left_i]
            else:
                right_j -= 1
                right_max = max(right_max, height[right_j])
                res += right_max - height[right_j]

        return res
