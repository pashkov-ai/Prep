from typing import List
import math


class Solution:
    """
    Provides a solution to determine the sum of all numbers in a list that
    have exactly four divisors. The class contains methods to efficiently
    compute divisors and calculate the desired sum based on the input numbers.

    This solution leverages caching to store divisor information for each
    evaluated number to improve performance when handling repeated elements
    in the input list.
    """
    def sumFourDivisors(self, nums: List[int]) -> int:
        """
        Calculates the sum of all numbers in the input list that have exactly
        four divisors. For each number with exactly four divisors, the sum
        of those divisors is added to the final result.

        :param nums: A list of integers to be checked for numbers with exactly four divisors.
        :type nums: List[int]
        :return: The sum of all divisors of numbers that have exactly four divisors.
        :rtype: int
        """

        def get_divs(num):
            divs = []
            d = 1
            while d*d <= num:
                if num % d == 0:
                    divs.append(d)
                    dd = num // d
                    if dd != d:
                        divs.append(dd)
                d += 1
            return divs

        div4_sum = 0
        div_count_map = {}
        for e in nums:
            if e not in div_count_map:
                divs = get_divs(e)
                div_count_map[e] = divs
            if len(div_count_map[e]) == 4:
                div4_sum += sum(div_count_map[e])
        return div4_sum


nums = [1,2,3,4,5,6,7,8,9,10]
r = Solution().sumFourDivisors(nums)
print(r)