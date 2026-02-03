from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            d = 1
            while nums[i] & d != 0:
                ans[i] = nums[i] - d
                d <<= 1
        return ans
