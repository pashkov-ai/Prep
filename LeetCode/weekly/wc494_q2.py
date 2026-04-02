class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # O(N) - time, O(1) - space
        n = len(nums1)
        min_even = math.inf
        min_odd = math.inf
        for e in nums1:
            is_even = e % 2 == 0
            if is_even:
                min_even = min(min_even, e)
            else:
                min_odd = min(min_odd, e)
        if min_even == 0 or min_odd == math.inf:
            return True
        if min_even >= min_odd + 1:
            return True
        return False