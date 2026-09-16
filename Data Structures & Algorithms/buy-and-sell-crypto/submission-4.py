class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        second = 1
        maxprofit = 0
        while left < len(prices) - 1 and second != len(prices):
            if prices[left] > prices[second]:
                left = second
            elif (prices[second] - prices[left]) > maxprofit:
                maxprofit = prices[second] - prices[left]
            second += 1

        return maxprofit
            