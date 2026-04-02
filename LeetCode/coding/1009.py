class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # O(1) - time, space
        if n == 0:
            return 1
        res = x = n
        base = 1
        while x > 0:
            res ^= base
            base <<= 1
            x >>= 1
        return res
