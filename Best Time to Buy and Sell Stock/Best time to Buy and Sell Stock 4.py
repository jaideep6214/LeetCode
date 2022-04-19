class Solution(object):
    def maxProfit(self, k, prices):
        if (k==0):
            return 0
        if (k>int (len(prices)//2)):
            left = 0
            right= 1
            ans = 0
            while (right < len(prices)):
                if (prices[right]>prices[left]):
                    ans = ans + prices[right]-prices[left]
                right+=1
                left+=1 
            return ans
        buys = [-99999 for i in range (k)]
        sells = [0 for i in range (k)]
 
        for price in prices:
            for i in range (k):
                if (i==0):
                    buys[i] = max (buys[i],-price)
                    sells[i] = max (sells[i], buys[i]+price)
                else:
                    buys[i] = max (buys[i],sells[i-1]-price)
                    sells[i] = max (sells[i], buys[i]+price)
        return (sells[-1])
        
