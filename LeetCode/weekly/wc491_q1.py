class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        # O(N) - time, O(1) - space
        vowels = {'a', 'e', 'i', 'o', 'u'}
        idx = len(s) - 1
        while idx >= 0 and s[idx] in vowels:
            idx -= 1
        return s[:idx + 1]

