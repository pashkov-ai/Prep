from collections import deque, namedtuple


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        BFSentry = namedtuple('BFSentry', ['x', 'y', 'depth'])
        seen = set()
        bfs_queue = deque()

        def add_cells_to_deque(coords: BFSentry, grid_size: int) -> None:
            x, y, d = coords
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < grid_size and 0 <= j < grid_size and grid[i][j] == 0 and (i, j) not in seen:
                        bfs_queue.append(BFSentry(i, j, d + 1))
                        seen.add((i, j))
            return

        n = len(grid)
        tx = ty = n - 1
        bfs_queue.append(BFSentry(tx, ty, 1))
        seen.add((tx, ty))
        while bfs_queue:
            bfs_entry = bfs_queue.pop()
            if bfs_entry.x == 0 and bfs_entry.y == 0:
                return bfs_entry.depth
            add_cells_to_deque(bfs_entry, n)
        return -1



