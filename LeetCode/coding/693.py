class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        cur_bit = 1 - n & 1
        last_bit = None
        x = n
        while x > 0:
            last_bit = cur_bit
            cur_bit = x & 1
            x >>= 1
            if cur_bit == last_bit:
                return False
        return True
