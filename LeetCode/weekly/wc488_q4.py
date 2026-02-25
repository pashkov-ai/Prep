import math

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        # tabula[i][j][h]
        # tabula = [[[-math.inf] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        tabula_prev = [[0.0] * (m + 1) for _ in range(n + 1)]
        tabula_curr = [[-math.inf] * (m + 1) for _ in range(n + 1)]

        for h in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    tabula_curr[i][j] = max(
                        tabula_curr[i - 1][j],
                        tabula_curr[i][j - 1],
                        tabula_prev[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]
                    )
                    tabula_prev[i - 1][j - 1] = -math.inf
            for i in range(n + 1):
                tabula_prev[i][m] = -math.inf
            for j in range(m + 1):
                tabula_prev[n][j] = -math.inf
            tabula_prev, tabula_curr = tabula_curr, tabula_prev
        return 0 if math.isinf(tabula_prev[n][m]) else int(tabula_prev[n][m])
