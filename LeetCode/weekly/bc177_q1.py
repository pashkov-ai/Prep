from collections import defaultdict


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        # O(N^2) - time, O(N) - space
        freqs = defaultdict(int)
        for e in nums:
            freqs[e] += 1
        sunums = sorted(freqs.keys())
        for i in range(len(sunums)):
            for j in range(i+1, len(sunums)):
                if freqs[sunums[i]] != freqs[sunums[j]]:
                    return [sunums[i], sunums[j]]
        return [-1, -1]