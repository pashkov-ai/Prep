class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # O(N) - time, space
        monostack = []  # O(N) - space
        discounted_prices = [-1] * len(prices)
        for i in range(len(prices)): # O(N) - time
            while monostack and prices[i] <= prices[monostack[-1]]:
                j = monostack.pop()
                discounted_prices[j] = prices[j] - prices[i]
            monostack.append(i)
        while monostack:
            j = monostack.pop()
            discounted_prices[j] = prices[j]
        return discounted_prices