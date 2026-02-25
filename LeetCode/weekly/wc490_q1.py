class Solution:
    def scoreDifference(self, nums: list[int]) -> int:

        def is_first_active_player(nums: list[int], i: int, is_first_active: bool) -> bool:
            is_6th_game = (i + 1) % 6 == 0
            if is_6th_game:
                is_first_active = not is_first_active

            is_odd = nums[i] & 1 == 1
            if is_odd:
                is_first_active = not is_first_active
            return is_first_active

        scores = {True: 0, False: 0}
        is_first_active = True
        for i in range(len(nums)):
            is_first_active = is_first_active_player(nums, i, is_first_active)
            scores[is_first_active] += nums[i]
        return scores[True] - scores[False]
