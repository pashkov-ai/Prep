class Solution:
    def minPartitions(self, n: str) -> int:
        # O(N) - time, O(1) - space
        max_digit = 0
        for c in n:
            max_digit = max(max_digit, int(c))
        return max_digit