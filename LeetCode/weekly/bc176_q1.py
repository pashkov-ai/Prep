class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        # O(WC) - time, O(1) - space, W - # words, C - avg length of the words
        MODULO = len(weights)
        result = []
        for word in words:
            word_weight = 0
            for c in word:
                word_weight += weights[ord(c) - ord('a')]
                word_weight %= MODULO
            result.append(chr(ord('z') - word_weight))
        return ''.join(result)
