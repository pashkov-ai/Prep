class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        memo = {}

        def dp(k: int, i: int, j: int) -> int:
            if k == m:
                return 0
            if k not in memo:
                memo[k] = {}
            if k in memo and (i,j) in memo[k]:
                return memo[k][(i,j)]

            mult = multipliers[k]
            memo[k][(i,j)] = max(
                mult*nums[i] + dp(k+1, i+1, j),
                mult*nums[j] + dp(k+1, i, j-1)
            )
            return memo[k][(i,j)]

        return dp(0, 0, len(nums)-1)