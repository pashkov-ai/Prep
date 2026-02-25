class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # O(N log N)- time, O(N) - space
        if len(s) == 0:
            return s
        substrs = [] # O(N) - space
        balanced = anchor = 0
        for i, c in enumerate(s): # O(N) - time
            balanced += 1 if c == '1' else -1
            if balanced == 0:
                x = self.makeLargestSpecial(s[anchor+1: i]) # X - time, space
                substrs.append(f'1{x}0')
                anchor = i + 1
        substrs.sort(reverse=True) # O(N log N) - time
        return ''.join(substrs)