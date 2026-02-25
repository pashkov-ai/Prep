from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        min_coin = min(coins)

        def dp(i: int, a: int) -> int:
            if a == 0:
                return i
            if min_coin > a:
                return -1

            if i in memo and a in memo[i]:
                return memo[i][a]

            if i not in memo:
                memo[i] = {}

            r = [e for e in (dp(i+1, a-c) for c in coins) if e != -1]
            if len(r) == 0:
                memo[i][a] = -1
            else:
                memo[i][a] = min(r)
            return memo[i][a]

        x = dp(0, amount)
        print(memo)
        return x

r = Solution().coinChange([1], 1)
print(r)