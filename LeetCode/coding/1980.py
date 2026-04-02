class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        # O(N) - time, O(1) - space
        ans = []
        for i in range(len(nums)):
            bit = nums[i][i]
            ans.append('0' if bit == '1' else '1')
        return ''.join(ans)