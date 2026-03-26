class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=0
        max_profit = 0
        for i in range(1, len(prices), 1):
            lowestbuy = prices[j]
            profit = max(0, prices[i] - lowestbuy)
            if profit>max_profit:
                max_profit = profit
            if prices[i] < prices[j]:
                j=i
        return(max_profit)

# so thing to note here, dont get focused on the idea that you need to be looking at the buy prices frist. iterate through them focusing on the sell price and working out what the profit would be for that by looking at the previously lowest buy price aka the numbers all behind it. before you did it in a way of calculating the max of the numbers to the left which is good but as you have a pointer i going through the code just infront of it you can use this to track what the max is as finding max is exoensive over a list.


