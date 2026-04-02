class Solution:
    def minOperations(self, s: str) -> int:
        # O(N) - time, O(1) - space
        n = len(s)
        min_i, max_i = n, 0
        min_v, max_v = ord('z') + 1, ord('a') - 1
        is_sorted = True
        for i, c in enumerate(s):
            ord_c = ord(c)
            if is_sorted and i > 0 and c < s[i-1]:
                is_sorted = False
            if ord_c < min_v:
                min_i, min_v = i, ord_c
            if ord_c >= max_v:
                max_i, max_v = i, ord_c

        if is_sorted:
            return 0
        if n == 2:
            return -1
        if min_i == n - 1 and max_i == 0:
            return 3
        if min_i != 0 and max_i != n - 1:
            return 2
        return 1