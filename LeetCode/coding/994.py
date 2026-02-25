from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        def is_valid_coords(grid: list[list[int]], i: int, j: int) -> bool:
            len_i, len_j = len(grid), len(grid[0])
            return 0 <= i < len_i and 0 <= j < len_j

        def is_fresh(grid: list[list[int]], i: int, j: int) -> bool:
            return grid[i][j] == 1

        def is_rotten(grid: list[list[int]], i: int, j: int) -> bool:
            return grid[i][j] == 2

        def is_orange(grid: list[list[int]], i: int, j: int) -> bool:
            return is_fresh(grid, i, j) or is_rotten(grid, i, j)

        def init_bfs(grid: list[list[int]]):
            len_i, len_j = len(grid), len(grid[0])
            deq = deque()
            has_oranges = False
            for i in range(len_i):
                for j in range(len_j):
                    if is_orange(grid, i, j):
                        has_oranges = True
                    if is_rotten(grid, i, j):
                        deq.appendleft((i, j, 0))
            return deq, has_oranges

        def run_bfs(grid: list[list[int]], time_grid: list[list[int]], deq: deque) -> None:
            while deq:
                i, j, v = deq.pop()
                if not is_valid_coords(grid, i, j):
                    continue
                if is_orange(grid, i, j):
                    if v >= time_grid[i][j] and time_grid[i][j] != -1:
                        continue
                    time_grid[i][j] = v
                    v += 1
                    extend_list = [(i - 1, j, v), (i + 1, j, v), (i, j - 1, v), (i, j + 1, v)]
                    deq.extendleft(extend_list)
            pass

        def find_max_time(grid: list[list[int]], time_grid: list[list[int]]) -> int:
            max_time = 0
            len_i, len_j = len(grid), len(grid[0])
            for i in range(len_i):
                for j in range(len_j):
                    time = time_grid[i][j]
                    if is_fresh(grid, i, j) and time == -1:
                        return -1
                    max_time = max(max_time, time)
            return max_time

        len_i, len_j = len(grid), len(grid[0])
        deq, has_oranges = init_bfs(grid)
        if not deq:
            if has_oranges:
                return -1  # only freshes
            return 0  # no oranges

        time_grid = [[-1] * len_j for _ in range(len_i)]
        run_bfs(grid, time_grid, deq)
        time = find_max_time(grid, time_grid)
        return time
