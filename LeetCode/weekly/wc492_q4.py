class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        # O(N) - time, space
        prefix = [0] * (len(s) + 1)  # O(N) - space
        for i in range(1, len(prefix)):  # O(N) - time
            prefix[i] = prefix[i - 1] + int(s[i - 1] == '1')

        def divide_and_conquer(start_i: int, end_i: int) -> int:
            # O(1) - time, space
            # [start, end)
            substr = s[start_i: end_i]
            substr_len = end_i - start_i
            one_count = prefix[end_i] - prefix[start_i]
            cost = flatCost if one_count == 0 else substr_len * one_count * encCost

            if substr_len % 2 == 0:
                half_len = substr_len // 2
                cost_split = divide_and_conquer(start_i, end_i - half_len) + divide_and_conquer(start_i + half_len,
                                                                                                end_i)
                cost = min(cost, cost_split)
            return cost

        return divide_and_conquer(0, len(s))  # O(N) - time

