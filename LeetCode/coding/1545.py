class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # O(N) - time, O(1) - space
        invert_count = 0
        length = (1 << n) - 1

        while k > 1: # O(N) - time
            half_length = length // 2 + 1
            if k == half_length:
                return '1' if invert_count & 1 == 0 else '0'

            if k > half_length:
                k = length + 1 - k
                invert_count += 1
            length //= 2
        return '0' if invert_count & 1 == 0 else '1'