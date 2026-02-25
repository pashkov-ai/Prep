class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        # O(N log N log I) ~ O(N log N) - time, O(1) - space

        def get_bits_count(x: int):
            # O(log I) - time
            counter = 0
            while x > 0:
                counter += x & 1
                x >>= 1
            return counter

        return sorted(arr, key = lambda x: (get_bits_count(x), x)) # O(N log N) - time