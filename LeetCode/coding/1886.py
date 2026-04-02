class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        # O(N^2) - time, O(1) - space
        n = len(mat)
        eq0 = eq90 = eq180 = eq270 = True
        for i in range(n):
            for j in range(n):
                t = target[i][j]
                if eq0 and t != mat[i][j]:
                    eq0 = False
                if eq90 and t != mat[j][n-i-1]:
                    eq90 = False
                if eq180 and t != mat[n-i-1][n-j-1]:
                    eq180 = False
                if eq270 and t != mat[n-j-1][i]:
                    eq270 = False
                if not (eq0 or eq90 or eq180 or eq270):
                    break
        return eq0 or eq90 or eq180 or eq270
