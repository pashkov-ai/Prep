class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # O(K *(N-K)) - time, O(min(2**K, N - K)) - space
        n_strings = 2**k
        hash_set = set() # O(min(2**K, N - K)) - space
        for i in range(len(s) - k + 1):# O(N - K) - time
            substr = s[i: i + k]
            hash_set.add(substr) # O(K) - time
            if len(hash_set) == n_strings:
                return True
        return False
