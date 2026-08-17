class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #mujhe prices me low and high price find krna hai sath me condition honi chaiye
        # low ka index < index of high
        min_price, max_profit= float('inf'), 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
          
        return max_profit