class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        sa_max_len = 0
        for i in range(n):
            even, odd = set(), set()
            for j in range(i, n):
                even.add(nums[j]) if nums[j] & 1 == 0 else odd.add(nums[j])
                if len(even) == len(odd):
                    sa_max_len = max(sa_max_len, j - i + 1)
        return sa_max_len