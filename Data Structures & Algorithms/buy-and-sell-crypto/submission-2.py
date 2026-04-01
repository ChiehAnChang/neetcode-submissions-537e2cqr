class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0

       	prev, curr = 0, 1

       	while curr < len(prices):

       		if prices[prev] < prices[curr]:
       			res = max(res, prices[curr] - prices[prev])

       		else:
       			prev = curr

       		curr += 1

       	return res
