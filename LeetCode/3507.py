from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # brute-force

        # go over array, check if condition ismet, remember the adj pair
        # if conditionis not met, sum up the pair - continue
        op_counter = 0
        is_non_decreasing = False
        len_array = len(nums)
        while not is_non_decreasing:
            is_non_decreasing = True
            min_sum = float('inf')
            min_sum_i = -1
            for i in range(1, len_array):
                if nums[i - 1] > nums[i]:
                    is_non_decreasing = False
                adj_sum = nums[i - 1] + nums[i]
                if adj_sum < min_sum:
                    min_sum = adj_sum
                    min_sum_i = i - 1

            # sumup
            if not is_non_decreasing:
                nums[min_sum_i] = min_sum
                nums[min_sum_i + 1: len_array - 1] = nums[min_sum_i + 2: len_array]
                len_array -= 1
                op_counter += 1
        return op_counter