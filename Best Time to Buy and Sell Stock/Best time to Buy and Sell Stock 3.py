class Solution(object):
    def maxProfit(self, prices):
        buy1=-99999
        sell1=0
        buy2=-99999
        sell2=0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1+price)
            buy2 = max(buy2, sell1-price)
            sell2 = max(sell2, buy2+price)
        return (sell2)
