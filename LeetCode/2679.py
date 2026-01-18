class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        def argmax(arr):
            return max(enumerate(arr), key=lambda x: x[1])[0]

        nrows, ncols = len(nums), len(nums[0])
        score = 0
        for i in range(ncols):  # O(M)
            argmaxes = [argmax(row) for row in nums]  # O(MxN)
            maxes = []
            for amax, row in zip(argmaxes, nums):  # O(N)
                maxes.append(row[amax])
                row[amax] = -1
            score += max(maxes)  # O(N)
            # O(M x (MN+N+N)) = o(NMM)
        return score

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:  # O(N x M log M)
            row.sort()

        nrows, ncols = len(nums), len(nums[0])
        score = 0
        for j in range(ncols):  # O(M)
            score += max(row[j] for row in nums)  # O(N + N)
        return score

        # Sorting
        # O(N x M log M)
        # Seelct
        # O(M X N)