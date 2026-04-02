class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # O(NM) - time, O(N + M) - space
        n, m = len(str1), len(str2)
        word = ['a'] * (n + m - 1)
        is_set = [False] * (n + m - 1)
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if is_set[i + j] and word[i + j] != str2[j]:
                        return ""
                    word[i + j] = str2[j]
                    is_set[i + j] = True

        for i in range(n):
            if str1[i] == 'F':
                # is there different chars
                if any(str2[j - i] != word[j] for j in range(i, i + m)):
                    continue

                for k in range(i + m - 1, i - 1, -1):
                    if not is_set[k]:
                        word[k] = 'b'
                        break
                else:
                    return ""
        return "".join(word)
