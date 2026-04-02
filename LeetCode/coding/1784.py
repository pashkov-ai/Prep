class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # O(N) - time, O(1) - space
        for i in range(1, len(s)):
            if s[i - 1] == '0' and s[i] == '1':
                return False
        return True
