class Solution:
    def minCost(self, n: int) -> int:
        return sum(i for i in range(1, n)) # O(N) - time, O(1) - space