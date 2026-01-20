from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 1. Row and Column Prefix Sums
        row_ps = [[0] * (n + 1) for _ in range(m + 1)]
        col_ps = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                row_ps[r + 1][c + 1] = row_ps[r + 1][c] + grid[r][c]
                col_ps[r + 1][c + 1] = col_ps[r][c + 1] + grid[r][c]

        def check(r, c, k):
            # The target sum is the sum of the first row of this kxk square
            target = row_ps[r + 1][c + k] - row_ps[r + 1][c]

            # Check all rows
            for i in range(r + 1, r + k):
                if row_ps[i + 1][c + k] - row_ps[i + 1][c] != target:
                    return False

            # Check all columns
            for j in range(c, c + k):
                if col_ps[r + k][j + 1] - col_ps[r][j + 1] != target:
                    return False

            # Check main diagonal
            d1 = 0
            for i in range(k):
                d1 += grid[r + i][c + i]
            if d1 != target:
                return False

            # Check anti-diagonal
            d2 = 0
            for i in range(k):
                d2 += grid[r + i][c + k - 1 - i]
            if d2 != target:
                return False

            return True

        # Search from largest possible k down to 2
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if check(r, c, k):
                        return k

        return 1