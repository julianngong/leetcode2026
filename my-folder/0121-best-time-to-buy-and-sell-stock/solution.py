# =========================================================================
    # My Thought Process / Notes:
    #
    # THE MENTAL SHIFT (Sell-Focused):
    # Don't get stuck thinking you need to pin the "Buy" price first and scan 
    # forward for the best "Sell" price. Instead, reverse your thinking! 
    # Iterate through the array treating the current day 'i' as the SELL price. 
    #
    # THE LOGIC: 
    # "If I sell today, what is the most profit I could make?" 
    # It is simply today's price minus the absolute LOWEST buy price I have 
    # seen on any day before today.
    #
    # THE OPTIMIZATION (Avoiding O(N^2)):
    # Previously, I tried calculating the max/min of the numbers to the left by 
    # taking slices of the list. Doing `min(prices[:i])` inside a loop is heavily 
    # expensive because it scans the list over and over, causing a Time Limit Exceeded.
    # 
    # By using a pointer 'j' (or just a 'min_price' variable) to remember the 
    # lowest price we've passed so far, we update our tracker in O(1) time. 
    # This keeps the whole algorithm running in a blazing fast O(N) time!
    # =========================================================================
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        max_profit = 0
        
        for price in prices:
            # If we find a lower price, update our lowest_buy
            if price < lowest_buy:
                lowest_buy = price
            # Otherwise, check if selling today beats our max profit
            elif price - lowest_buy > max_profit:
                max_profit = price - lowest_buy
                
        return max_profit
    
    # stick to how you do it before with going through prices and not tracking the pointer and just tracking lowest buy price
    def maxProfitTry2(self, prices: List[int]) -> int:
        bd = 0
        res = 0
        for sd in range(1,len(prices)):
            if prices[sd-1] < prices[bd]:
                bd = sd-1
            res = max(prices[sd] - prices[bd], res)
        return res


