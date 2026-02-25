class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # D = R - L, O(D log R) = O(D) - time, O(1) - space
        # enough for 20 bits
        primes = {2, 3, 5, 7, 11, 13, 17, 19}  # O(1) - space
        result = 0
        for x in range(left, right + 1): # O(D) - time
            num = x
            bits_count = 0
            while num > 0: # O(log R) ~ O(log 10^6) ~ O(1) ~ 20
                bits_count += num & 1
                num >>= 1
            if bits_count in primes:
                result += 1
        return result