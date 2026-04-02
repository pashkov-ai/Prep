import math

class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        # O(MN) - time, space
        m, n = len(coins), len(coins[0])
        tabula = [[[-math.inf] * 3 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                c = coins[i][j]
                if i == 0 and j == 0:
                    tabula[0][0][0] = c
                    tabula[0][0][1] = 0 if c < 0 else -math.inf
                    continue

                if i != 0:
                    tabula[i][j][0] = max(tabula[i][j][0], tabula[i - 1][j][0] + c)
                    tabula[i][j][1] = max(tabula[i][j][1], tabula[i - 1][j][1] + c)
                    tabula[i][j][2] = max(tabula[i][j][2], tabula[i - 1][j][2] + c)
                    if c < 0:
                        tabula[i][j][1] = max(tabula[i][j][1], tabula[i - 1][j][0])
                        tabula[i][j][2] = max(tabula[i][j][2], tabula[i - 1][j][1])

                if j != 0:
                    tabula[i][j][0] = max(tabula[i][j][0], tabula[i][j - 1][0] + c)
                    tabula[i][j][1] = max(tabula[i][j][1], tabula[i][j - 1][1] + c)
                    tabula[i][j][2] = max(tabula[i][j][2], tabula[i][j - 1][2] + c)
                    if c < 0:
                        tabula[i][j][1] = max(tabula[i][j][1], tabula[i][j - 1][0])
                        tabula[i][j][2] = max(tabula[i][j][2], tabula[i][j - 1][1])
        return max(tabula[m - 1][n - 1])
