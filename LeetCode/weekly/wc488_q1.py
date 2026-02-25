class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        n = len(nums)
        counter = 0
        prefix_sum = nums[n-1]
        average_elems = 1
        for i in reversed(range(n-1)):
            if nums[i] * average_elems > prefix_sum:
                counter += 1
            average_elems += 1
            prefix_sum += nums[i]
        return counter


class SolutionNotPrecise:
    def dominantIndices(self, nums: list[int]) -> int:
        n = len(nums)
        counter = 0
        moving_average = nums[n-1]
        average_elems = 1
        for i in reversed(range(n-1)):
            if nums[i] > moving_average:
                counter += 1
            average_elems += 1
            moving_average += (nums[i] - moving_average) / average_elems
        return counter