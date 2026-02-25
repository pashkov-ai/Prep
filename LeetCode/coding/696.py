class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # O(N) - time, space
        n = len(s)
        counts_backward = [0] * n # O(N) - space
        counts_backward[n - 1] = 1
        for i in reversed(range(n - 1)): # O(N) - time
            if s[i] != s[i + 1]:
                counts_backward[i] = 1
            else:
                counts_backward[i] = counts_backward[i + 1] + 1

        bs_count = 0
        prev = 1
        for i in range(1, n): #O(N) - time
            # counting
            if s[i - 1] != s[i]:
                bs_count += min(prev, counts_backward[i])

            if s[i] != s[i - 1]:
                prev = 1
            else:
                prev += 1
        return bs_count
