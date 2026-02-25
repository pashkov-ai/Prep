from typing import List


# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         memo = {}
#
#         def dp(k: int, h: int, w: int):
#             # base case
#             if k == 1:
#                 return 1 if matrix[h][w] == '1' else 0
#
#             if k in memo and (h, w) in memo[k]:
#                 return memo[k][(h, w)]
#
#             if k not in memo:
#                 memo[k] = {}
#
#             mn = min(
#                 dp(k - 1, h - 1, w - 1),
#                 dp(k - 1, h - 1, w),
#                 dp(k - 1, h, w - 1),
#             )
#             mx = max(
#                 dp(k - 1, h - 1, w - 1),
#                 dp(k - 1, h - 1, w),
#                 dp(k - 1, h, w - 1),
#             )
#             if mn == k - 1 and dp(1, h, w) == 1:
#                 v = k
#             else:
#                 v = max(mx, dp(k-1, h, w))
#             # recursion
#             memo[k][(h, w)] = v
#             return memo[k][(h, w)]
#
#         square_size = min(m, n)
#         sizes = []
#         if n > m:
#             for j in range(square_size-1, n):
#                 s = dp(square_size, m - 1, j)
#                 sizes.append(s)
#         else:
#             for i in range(square_size-1, m):
#                 s = dp(square_size, i, n - 1)
#                 sizes.append(s)
#
#         return max(sizes) ** 2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        tabula = [[0] * n for _ in range(m)]

        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0

            if i in tabula and j in tabula[i]:
                return tabula[i][j]

            if matrix[i][j] == '0':
                tabula[i][j] = 0
                return 0

            tabula[i][j] = min(dp(i - 1, j - 1), dp(i - 1, j), dp(i, j - 1)) + 1
            return tabula[i][j]

        dp(m - 1, n - 1)
        print(tabula)
        mx = max(max(tabula[i]) for i in range(m))
        return mx * mx

Solution().maximalSquare([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])