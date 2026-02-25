class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solution method

        :param nums: list of houses' values

        :return: max robbery value
        """

        def dp(i: int) -> int:
            """
            DP solution to the problem

            :param i: ith house
            :return: max robbery value at ith house
            """
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i - 2) + nums[i], dp(i - 1))
            return memo[i]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        return dp(len(nums) - 1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solution method

        :param nums: list of houses' values

        :return: max robbery value
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        tabula = [0] * len(nums)
        tabula[0] = nums[0]
        tabula[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tabula[i] = max(tabula[i - 2] + nums[i], tabula[i - 1])
        return tabula[len(nums) - 1]

