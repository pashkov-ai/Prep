class Solution:
    def countCommas(self, n: int) -> int:
        # O(1) - time, space
        if n < 1000:
            return 0
        if n < 100_000:
            return n - 999
        return n - 999
