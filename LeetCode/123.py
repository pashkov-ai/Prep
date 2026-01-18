from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        max_transactions = 2
        tabula = [[0] * (len(prices) + 1) for _ in range(max_transactions + 1)]
        # pric| 6 1 3 2 4 7
        # k\i | 0 1 2 3 4 5
        #     | -----------
        # 0   | 0 0 0 0 0 0
        # 1   | 0 0 2 2 3 6
        # 2   | 0 0 2 2 4 7

        mn = prices[0]
        for i in range(1, len(prices)):
            tabula[1][i] = max(tabula[1][i - 1], prices[i] - mn)
            mn = min(mn, prices[i])

        for i in range(1, len(prices)):
            for j in range(1, i):
                tabula[2][i] = max(tabula[2][i], tabula[2][i - 1], tabula[1][j] + prices[i] - prices[j])

        return max(tabula[1][len(prices) - 1], tabula[2][len(prices) - 1])

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # [7 1 5 3 6]
        # [0 0 4 4 5]
        # [5 5 3 3 0]
        left_profits = [0] * (len(prices) + 1)
        right_profits = [0] * (len(prices) + 1)  # +1 for convinience
        max_profits = [0] * (len(prices) + 1)

        min_price_left = float('inf')
        for i in range(1, len(prices) + 1):
            left_profits[i] = max(left_profits[i - 1], prices[i - 1] - min_price_left)
            min_price_left = min(min_price_left, prices[i - 1])

        max_price_right = float('-inf')
        for j in reversed(range(0, len(prices))):
            right_profits[j] = max(right_profits[j + 1], max_price_right - prices[j])
            max_price_right = max(max_price_right, prices[j])

        for i in range(len(max_profits)):
            max_profits[i] = left_profits[i] + right_profits[i]
        return max(max_profits)

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost = t2_cost = float('inf')
        t1_profit = t2_profit = 0

        for i in range(len(prices)):
            t1_cost = min(t1_cost, prices[i])
            t1_profit = max(t1_profit, prices[i] - t1_cost)

            t2_cost = min(t2_cost, prices[i] - t1_profit)
            t2_profit = max(t2_profit, prices[i] - t2_cost)
        return t2_profit


