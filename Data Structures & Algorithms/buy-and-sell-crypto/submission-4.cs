public class Solution
{
    public int MaxProfit(int[] prices)
    {
        if (prices == null || prices.Length == 0)
        {
            return 0;
        }

        int profit = 0;
        int currMin = prices[0];

        foreach (int price in prices)
        {
            if (price < currMin)
            {
                currMin = price;
            }
            else
            {
                profit = Math.Max(price - currMin, profit);
            }
        }

        return profit;
    }
}