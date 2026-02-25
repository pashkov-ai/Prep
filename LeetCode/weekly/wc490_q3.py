class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        one_bin_count_in_t = sum(b == '1' for b in t)

        max_bin_str = [''] * len(s)
        for i, b in enumerate(s):
            if one_bin_count_in_t == 0:
                max_bin_str[i] = s[i]
                continue
            if b == '0':
                one_bin_count_in_t -= 1
            max_bin_str[i] = '1'

        i = len(s) - 1
        while one_bin_count_in_t > 0:
            if s[i] == '1':
                max_bin_str[i] = '0'
                one_bin_count_in_t -= 1
            i -= 1
        return ''.join(max_bin_str)