class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        # calculate row-wise prefix sums
        m, n = len(mat), len(mat[0] if len(mat) > 0 else 0)
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j] + mat[i][j]

        def get_square_sum(si: int, sj: int, k: int) -> int:
            square_sum = (
                prefix_sum[si + k][sj + k]
                - prefix_sum[si + k][sj] 
                - prefix_sum[si][sj + k]
                + prefix_sum[si][sj]
            )
            return square_sum

        # for each cell
        # go over each available k, starting wiht max_side_length
        # calculate square sum using prefixs, update max_side_length if sum <= th else continue to next cell
        max_side_length_th = 0
        for i in range(m):
            for j in range(n):
                max_square_side = min(m - i, n - j)
                for k in range(max_side_length_th + 1, max_square_side + 1):
                    square_sum = get_square_sum(i, j, k)
                    if square_sum <= threshold:
                        max_side_length_th = k
                    else:
                        break
        return max_side_length_th