class Solution:
    def isDecomposable(self, s: str) -> bool:
        has_string_diff_2 = False
        l = 1
        for i in range(1, len(s)+1):
            c = s[i] if i != len(s) else '?'
            if c == s[i-1]:
                l += 1
            else:
                if l % 3 != 0:
                    if (l-2) % 3 != 0:
                        return False
                    else:
                        if  has_string_diff_2:
                            return False
                        else:
                            has_string_diff_2 = True
                l = 1
        return has_string_diff_2