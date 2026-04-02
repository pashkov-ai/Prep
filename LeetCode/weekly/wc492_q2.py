class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        # O(N) - time, O(N) - space
        n = len(nums)
        sums = [0] * n
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i-1]

        sums_sum = sum(sums)
        min_idx = -1
        rolling_prod = 1
        for i in reversed(range(n)):
            if rolling_prod == sums[i]:
                min_idx = i
            if rolling_prod < sums_sum or nums[i] == 0:
                rolling_prod *= nums[i]
        return min_idx