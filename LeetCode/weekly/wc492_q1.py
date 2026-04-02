import math

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        # O(N) - time, O(1) - space
        min_box_size = math.inf
        min_box_idx = -1
        for i, c in enumerate(capacity):
            if c < min_box_size and c >= itemSize:
                min_box_idx, min_box_size = i, c
        return min_box_idx
