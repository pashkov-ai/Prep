class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        # O(NM) - time, space
        n, m = len(grid), len(grid[0])
        prefix_sum = [[0] * (m+1) for _ in range(n+1)]

        counter = 0
        for i in range(n):
            for j in range(m):
                prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j] + grid[i][j]
                if prefix_sum[i+1][j+1] <= k:
                    counter += 1
                else:
                    break
        return counter