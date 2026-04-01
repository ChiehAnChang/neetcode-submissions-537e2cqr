class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        left_i, right_j = 0, 1
        curr_max = 0
        while right_j < len(prices):

            left, right = prices[left_i], prices[right_j]

            if left < right:
                curr_max = max(curr_max, right - left)
            else:
                left_i = right_j
            
            right_j += 1
        
        return curr_max