class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        # O(MN) - time, O(1) - space
        m, n = len(mat), len(mat[0])
        k %= n
        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True

