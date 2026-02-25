from collections import deque
from dataclasses import dataclass, field
import math


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        def get_cost(mn: int, mx: int, l: int, r: int) -> int:
            return (mx - mn) * (r - l + 1)

        min_monoq = deque()  # nums[i] <= nums[i+1] for i in q
        max_monoq = deque()  # nums[i] >= nums[i+1] for i in q
        left = 0
        counter = 0
        for right, num in enumerate(nums):
            # maintain monoq invariants
            while min_monoq and nums[min_monoq[-1]] > num:
                min_monoq.pop()
            while max_monoq and nums[max_monoq[-1]] < num:
                max_monoq.pop()
            min_monoq.append(right)
            max_monoq.append(right)

            # shrink window to satisfy K
            while min_monoq and max_monoq and get_cost(nums[min_monoq[0]], nums[max_monoq[0]], left, right) > k:
                # compare indicies in monoqs and move left by 1 to maintain condition
                if min_monoq[0] == left:
                    min_monoq.popleft()
                if max_monoq[0] == left:
                    max_monoq.popleft()
                left += 1

            counter += right - left + 1
        return counter


@dataclass
class MinMax:
    mn: float = field(default=math.inf)
    mx: float = field(default=-math.inf)

class SolutionNaive:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # O(N^2) - time, O(N^2) - space
        # 1 3 2
        #
        answer = 0
        n = len(nums)
        minmax = [[MinMax() for _ in range(n)] for _ in range(n)] # O(N^2) - space, time
        for i in range(n): # O(N) - time
            for j in range(i, n): # O(N) - time
                if i == j:
                    minmax[i][j].mn = nums[j]
                    minmax[i][j].mx = nums[j]
                    answer += 1
                    continue
                minmax[i][j].mn = min(minmax[i][j-1].mn, nums[j])
                minmax[i][j].mx = max(minmax[i][j-1].mx, nums[j])
                # print(nums[j], minmax[i][j])
                cost = (minmax[i][j].mx - minmax[i][j].mn) * (j - i + 1)
                # print(cost)
                if cost <= k:
                    answer += 1
        return answer

ans = Solution().countSubarrays([1,3,2], 4)
print(ans)