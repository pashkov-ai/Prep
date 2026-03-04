class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        # O(N) - time, space
        char_idx = {}  # O(N) - space
        offset = 0
        result = []
        for i, c in enumerate(s):  # O(N) - time
            if c not in char_idx:
                result.append(c)
                char_idx[c] = len(result) - 1
                continue
            last_char_occurence = char_idx[c]
            diff = i - last_char_occurence - offset
            if diff > k:  # update idx if outside window
                result.append(c)
                char_idx[c] = len(result) - 1
            else:
                offset += 1
        return ''.join(result)

