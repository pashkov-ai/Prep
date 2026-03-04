from collections import defaultdict


class Solution:
    def prefixConnected(self, words: list[str], k: int) -> int:
        # O(N) - time, space
        prefix_count_map = defaultdict(int) # O(N) - space
        for word in words: # O(N) - time
            if len(word) < k:
                continue
            prefix = word[:k]
            prefix_count_map[prefix] += 1
        return sum(v > 1 for v in prefix_count_map.values()) # O(N) - time