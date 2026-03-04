class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        # O(N) - time, O(1) - space
        N_BULBS = 100
        is_bulb_on = [False] * (N_BULBS + 1)
        for b in bulbs:  # O(N)
            is_bulb_on[b] = not is_bulb_on[b]
        return [i for i, x in enumerate(is_bulb_on) if x]
