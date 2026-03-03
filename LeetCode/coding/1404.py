class Solution:
    def numSteps(self, s: str) -> int:
        # convert to int
        b = 0
        base = 1
        for i, c in enumerate(reversed(s)):
            b += base if c == '1' else 0
            base <<= 1

        counter = 0
        while b != 1:
            if b & 1 == 0:  # even
                b >>= 1
            else:  # odd
                b += 1
            counter += 1
        return counter

