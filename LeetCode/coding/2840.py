from collections import defaultdict

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # O(N) - time, O(A) - space
        n = len(s1)
        s1_map, s2_map = {0: defaultdict(int), 1: defaultdict(int)}, {0: defaultdict(int), 1: defaultdict(int)}
        for i in range(n):
            k = i % 2
            s1_map[k][s1[i]] += 1
            s2_map[k][s2[i]] += 1
        for k in range(2):
            if s1_map[k].keys() != s2_map[k].keys():
                return False
            for c in s1_map[k].keys():
                if s1_map[k][c] != s2_map[k][c]:
                    return False
        return True


