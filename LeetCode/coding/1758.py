class Solution:
    def minOperations(self, s: str) -> int:
        # O(N) - time, O(1) - space
        patterns = {'01': 0, '10': 0}
        for i, c in enumerate(s):  # O(N) - time
            idx = i % 2
            for k in patterns.keys():
                pbit = k[idx]
                if pbit != c:
                    patterns[k] += 1
        return min(patterns.values())
