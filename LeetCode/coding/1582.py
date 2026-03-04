class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        # O(NM) - time, O(N + M) - space
        m, n = len(mat), len(mat[0])
        candidates = []
        elim_rows = [False] * m
        elim_cols = [False] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 1:
                    continue
                if elim_rows[i] or elim_cols[j]:
                    for t in reversed(range(len(candidates))):
                        ki, kj = candidates[t]
                        if i == ki and elim_rows[ki] or j == kj and elim_cols[kj]:
                            del candidates[t]
                else:
                    candidates.append((i, j))
                elim_rows[i] = True
                elim_cols[j] = True
        return len(candidates)
