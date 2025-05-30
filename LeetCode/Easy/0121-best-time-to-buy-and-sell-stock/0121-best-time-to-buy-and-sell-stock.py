class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최댓값과 최솟값을 계속 갱신
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        
        return profit