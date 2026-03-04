class Solution:
    def reverseBits(self, n: int) -> int:
        # O(1) - time, space
        x = n
        r = 0
        for _ in range(32):
            bit = x & 1
            x >>= 1
            r <<= 1
            r |= bit
        return r