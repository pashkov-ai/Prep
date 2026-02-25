from collections import defaultdict
from math import gcd


class Solution:
    def countSequences(self, nums: list[int], k: int) -> int:
        # O(N * S) - time, O(S) - space
        dp = {}  # O(S) - space
        dp[(1, 1)] = 1  # (p / q) = n - ways to get the ratio

        for e in nums:  # O(N) - time
            new_dp = defaultdict(int)
            for (p, q), c in dp.items():  # O(S) - time
                # skip
                new_dp[(p, q)] += c

                # mult
                mp, mq = p * e, q
                g = gcd(mp, mq) # O(log max(p, q))
                new_dp[(mp // g, mq // g)] += c

                # div
                mp, mq = p, q * e
                g = gcd(mp, mq)
                new_dp[(mp // g, mq // g)] += c

            dp = new_dp

        return dp[(k, 1)]