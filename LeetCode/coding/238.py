class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # O(N) - time, O(1) - space
        n = len(nums)
        prefix = 1
        answer = [1] * (n+1)

        for i in reversed(range(n)):
            answer[i] = answer[i+1] * nums[i]

        for i in range(n):
            answer[i] = prefix * answer[i+1]
            prefix *= nums[i]

        return answer[:n]