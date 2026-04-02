class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # O(K**2) - time, O(1) - space
        for r in range(k // 2):
            for c in range(k):
                swap_up_i = x + r
                swap_down_i = x + k - r -1
                swap_j = y + c
                grid[swap_up_i][swap_j], grid[swap_down_i][swap_j] = grid[swap_down_i][swap_j], grid[swap_up_i][swap_j]
        return grid
