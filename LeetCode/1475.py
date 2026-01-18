class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        monostack = []
        pricemap = {}
        for i, p in enumerate(prices):
            while monostack and p <= monostack[-1][1] and i > monostack[-1][0]:
                pricemap[monostack.pop()[0]] = p
            monostack.append((i, p))
        answer = [p - pricemap.get(i, 0) for i, p in enumerate(prices)]
        return answer