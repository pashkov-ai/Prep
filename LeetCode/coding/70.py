class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution to the Climb Stairs problem

        :param n: number of stairs in the ladder

        :return: number of ways the nth stair can be reached
        """
        memo = {1: 1, 2: 2}

        def dp(i:int) -> int:
            """
            dp solution to the problem
            :param i: - step number

            :return: n of ways the ith step can be reached
            """
            if i in memo:
                return memo[i]
            memo[i] = dp(i-2) + dp(i-1)
            return memo[i]

        return dp(n)

    class Solution:
        def climbStairs(self, n: int) -> int:
            """
            Solution to the Climb Stairs problem

            :param n: number of stairs in the ladder

            :return: number of ways the nth stair can be reached
            """
            tabula = [i + 1 for i in range(n)]

            for i in range(2, n):
                tabula[i] = tabula[i - 2] + tabula[i - 1]
            return tabula[n - 1]