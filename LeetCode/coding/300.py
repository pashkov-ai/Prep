from typing import List

#todo: bisect, inttelij

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tabula = [1] * len(nums) # Space: O(N)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    tabula[i] = max(tabula[i], tabula[j] + 1)
        return max(tabula)

