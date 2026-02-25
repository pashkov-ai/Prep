class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        first = second = 0
        x = n
        i = 0
        one_counter = 0
        while x > 0:
            bit = x & 1
            if bit:
                first, second = i, first
                one_counter += 1
                if one_counter >= 2:
                    max_dist = max(max_dist, first - second)
            x >>= 1
            i += 1
        return max_dist
