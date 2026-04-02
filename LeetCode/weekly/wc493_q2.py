class Solution:
    def countCommas(self, n: int) -> int:
        # O(log N) - time, O(1) - space
        digit_count = 0
        x = n
        while x > 0:
            x //= 10
            digit_count += 1

        commas_counter = 0
        if digit_count == 16:
            commas_counter += 1
        if digit_count >= 13:
            commas_counter += n - 999_999_999_999
        if digit_count >= 10:
            commas_counter += n - 999_999_999
        if digit_count >= 7:
            commas_counter += n - 999_999
        if digit_count >= 4:
            commas_counter += n - 999
        return commas_counter
