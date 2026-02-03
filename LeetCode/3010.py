from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_cost = nums[0]
        # go over array from 1..n-1 and find 2 min values
        min1, min2 = min(nums[1], nums[2]), max(nums[1], nums[2])
        for e in nums[3:]:
            if e < min1:
                min1, min2 = e, min1
            elif e < min2:
                min2 = e

        min_cost += min1 + min2
        return min_cost