class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        # O(N) - time, O(1) - space
        i = j = -1
        ans = math.inf
        for h, e in enumerate(nums):
            if e == 1:
                i = h
            if e == 2:
                j = h

            if i != -1 and j != -1:
                ans = min(ans, abs(i - j))
        return ans if ans != math.inf else -1