import heapq

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        char_freq = {}
        for c in s:
            char_freq[c] = char_freq.setdefault(c, 0) + 1
        dk = len(char_freq) - k
        if dk <= 0:
            return 0
        minheap = [f for c, f in char_freq.items()]
        heapq.heapify(minheap)
        return sum(heapq.nsmallest(dk, minheap))