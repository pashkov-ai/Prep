class Solution:
    def rob(self, nums: list[int], colors: list[int]) -> int:
        # O(N) - time, O(1) - space
        n = len(nums)
        dp2, dp1, dp = 0, nums[0], nums[0]
        for i in range(1, n):
            value = nums[i] if colors[i] != colors[i-1] else 0
            dp = max(dp1 + value, dp2 + nums[i])
            dp2, dp1 = dp1, dp
        return dp