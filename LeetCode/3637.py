from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        switch_counter = {True: 0, False: 0}
        is_increasing = nums[0] < nums[1]
        switch_counter[is_increasing] += 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False
            if nums[i] < nums[i+1] and not is_increasing:
                is_increasing = True
                switch_counter[is_increasing] += 1
            if nums[i] > nums[i+1] and is_increasing:
                is_increasing = False
                switch_counter[is_increasing] += 1
        return switch_counter[True] == 2 and switch_counter[False] == 1 