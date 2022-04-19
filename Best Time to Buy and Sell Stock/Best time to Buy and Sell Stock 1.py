class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right= 1
        ans = 0
        while (right < len(prices)):
            if (prices[right]<prices[left]):
                left = right
            elif (prices[left]<prices[right]):
                ans1=prices[right]-prices[left]
                if (ans1 > ans):
                    ans=ans1
            right+=1
        return ans
        
