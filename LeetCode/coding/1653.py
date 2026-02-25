class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_dels = b_count = 0
        for c in s:
            if c == 'b':
                b_count += 1
            else:
                min_dels = min(min_dels + 1, b_count)
        return min_dels