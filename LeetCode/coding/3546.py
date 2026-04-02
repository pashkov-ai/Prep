class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        # O(NM) - time, O(N + M) - space
        m, n = len(grid), len(grid[0])
        prefix_sum_rows = [0] * m
        prefix_sum_cols = [0] * n

        for i in range(m):
            for j in range(n):
                prefix_sum_rows[i] += grid[i][j]
                prefix_sum_cols[j] += grid[i][j]

        # make suffix sums
        suffix_rows = [0] * (m + 1)
        for i in reversed(range(m)):
            suffix_rows[i] = suffix_rows[i + 1] + prefix_sum_rows[i]

        suffix_cols = [0] * (n + 1)
        for j in reversed(range(n)):
            suffix_cols[j] = suffix_cols[j + 1] + prefix_sum_cols[j]

        # horizontal cuts
        prefix_h = 0
        for i in range(m - 1):
            prefix_h += prefix_sum_rows[i]
            if prefix_h == suffix_rows[i + 1]:
                return True

        prefix_v = 0
        for j in range(n - 1):
            prefix_v += prefix_sum_cols[j]
            if prefix_v == suffix_cols[j + 1]:
                return True

        return False

