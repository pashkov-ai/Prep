from typing import List

#TODO trie


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tabula = [False] * (len(s) + 2)
        tabula[len(s)] = True
        for i in reversed(range(0, len(s))):
            substr = s[i:]
            for word in wordDict:
                tabula[i] = max(tabula[i], tabula[min(i+len(word), len(s)+1)] and substr.startswith(word))
        return tabula[0]