class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:

        digit_factorials = [1] * 10
        for i in range(2, 10):
            digit_factorials[i] = digit_factorials[i-1] * i

        n_digit_count = [0] * 10
        fact_sum = 0
        x = n
        while x > 0:
            d = x % 10
            x //= 10
            n_digit_count[d] += 1
            fact_sum += digit_factorials[d]

        fact_sum_digit_count = [0] * 10
        x = fact_sum
        while x > 0:
            d = x % 10
            x //= 10
            fact_sum_digit_count[d] += 1

        for x, y in zip(n_digit_count, fact_sum_digit_count):
            if x != y:
                return False
        return True