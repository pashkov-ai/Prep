class Solution:
    # O(N * K) | O(N * 2**N), O(N) - space (stack)
    i = 0
    result_str = ''

    def getHappyString(self, n: int, k: int) -> str:
        charset = "abc"

        def rec(cur_string: str) -> None:
            if self.i == k:
                return
            last_char = cur_string[-1] if len(cur_string) > 0 else ''
            for c in charset:
                if c == last_char:
                    continue
                new_str = cur_string + c
                if len(new_str) == n:
                    self.result_str = new_str
                    self.i += 1
                    if self.i == k:
                        return
                else:
                    rec(new_str)
            pass

        rec('')
        return self.result_str if k == self.i else ''