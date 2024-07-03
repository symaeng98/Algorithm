class Solution(object):
    def maxProfit(self, prices):
        left = 0
        result = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                if result < prices[right]-prices[left]:
                    result = prices[right]-prices[left]
        return result