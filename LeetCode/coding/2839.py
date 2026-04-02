class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s21 = s2[2] + s2[1] + s2[0] + s2[3]
        s22 = s2[0] + s2[3] + s2[2] + s2[1]
        s23 = s2[2] + s2[3] + s2[0] + s2[1]
        return s1 == s2 or s1 == s21 or s1 == s22 or s1 == s23