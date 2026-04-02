class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        # O(NM) - time, space
        n, m = len(grid), len(grid[0])
        prefix_X = [[0] * (m + 1) for _ in range(n + 1)]
        prefix_Y = [[0] * (m + 1) for _ in range(n + 1)]

        counter = 0
        # calculate prefixes
        for i in range(n):
            for j in range(m):
                is_X = grid[i][j] == 'X'
                is_Y = grid[i][j] == 'Y'
                prefix_X[i + 1][j + 1] = prefix_X[i + 1][j] + prefix_X[i][j + 1] - prefix_X[i][j] + is_X
                prefix_Y[i + 1][j + 1] = prefix_Y[i + 1][j] + prefix_Y[i][j + 1] - prefix_Y[i][j] + is_Y
                if prefix_X[i + 1][j + 1] > 0 and prefix_X[i + 1][j + 1] == prefix_Y[i + 1][j + 1]:
                    counter += 1
        return counter
