from typing import List

class Solution: # TLE
    def maxProfit(self, k: int, prices: List[int]) -> int:
        tabula = [[0]*(len(prices)+1) for _ in range(k+1)]
        # pric| 6 1 3 2 4 7
        # k\i | 0 1 2 3 4 5
        #     | -----------
        # 0   | 0 0 0 0 0 0
        # 1   | 0 0 2 2 3 6
        # 2   | 0 0 2 2 4 7

        mn = prices[0]
        for i in range(1, len(prices)):
            tabula[1][i] = max(tabula[1][i-1], prices[i]-mn)
            mn = min(mn, prices[i])

        for c in range(2, k+1):
            for i in range(1, len(prices)):
                for j in range(1, i):
                    tabula[c][i] = max(tabula[c][i], tabula[c][i-1], tabula[c-1][j] + prices[i]-prices[j])

        return max(tabula[c][len(prices)-1] for c in range(k+1))



class Solution: # game simulation, coool
    def maxProfit(self, k: int, prices: List[int]) -> int:
        costs = [float('inf')] * (k+1)
        profits = [0] * (k+1)
        for price in prices:
            # c0 = min(c0, prices[i] - 0)
            # p0 = max(p0, prices[i] - c0)
            # c1 = min(c1, prices[i] - p0)
            # p1 = max(p1, prices[i] - c1)
            for q in range(1, k+1):
                costs[q] = min(costs[q], price - profits[q-1])
                profits[q] = max(profits[q], price - costs[q])
        return profits[-1]
