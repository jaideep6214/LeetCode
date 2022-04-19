class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right= 1
        ans = 0
        while (right < len(prices)):
            if (prices[right]>prices[left]):
                ans = ans + prices[right]-prices[left]
            right+=1
            left+=1 
        return ans
