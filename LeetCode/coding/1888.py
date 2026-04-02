class Solution:
    def minFlips(self, s: str) -> int:
        # O(N) - time, O(1) - space
        patterns = ['01', '10']
        counters = [0] * 2
        res = len(s)

        for i in range(len(s)):
            counters[0] += 1 if patterns[0][i % 2] != s[i] else 0
            counters[1] += 1 if patterns[1][i % 2] != s[i] else 0

        for i in range(len(s)):
            counters[0] -= 1 if patterns[0][i % 2] != s[i] else 0
            counters[1] -= 1 if patterns[1][i % 2] != s[i] else 0
            counters[0] += 1 if patterns[0][(i + (len(s) % 2)) % 2] != s[i] else 0
            counters[1] += 1 if patterns[1][(i + (len(s) % 2)) % 2] != s[i] else 0
            res = min(res, min(counters))
        return res