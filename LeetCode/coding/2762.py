from collections import deque

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        MAX_DIFF = 2
        min_monoq = deque() # n[i] <= n[i+1] 
        max_monoq = deque() # n[i] >= n[i+1]
        left = 0
        counter = 0
        for right, num in enumerate(nums):
            #maintain monoqs invariants
            while min_monoq and nums[min_monoq[-1]] > num:
                min_monoq.pop()
            while max_monoq and nums[max_monoq[-1]] < num:
                max_monoq.pop()
            min_monoq.append(right)
            max_monoq.append(right)

            # maintain CSA condition by moving left pointer
            while nums[max_monoq[0]] - nums[min_monoq[0]] > MAX_DIFF:
                # comparing indicies of original nums stored in monoqs
                left = min_monoq.popleft() if min_monoq[0] < max_monoq[0] else max_monoq.popleft()
                left += 1
            counter += right - left + 1
        return counter