class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        # O(N^2) - time, O(1) - space*
        MODULO = 12345
        n, m = len(grid), len(grid[0])
        product = [[1] * m for _ in range(n)]

        suffix = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                product[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MODULO

        prefix = 1
        for i in range(n):
            for j in range(m):
                product[i][j] = (prefix * product[i][j]) % MODULO
                prefix = (prefix * grid[i][j]) % MODULO

        return product
