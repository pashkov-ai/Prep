from collections import deque

class Solution:
    def mergeAdjacent(self, nums: list[int]) -> list[int]:
        # O(N) - time, space
        # 2 1 1 4
        #       ^
        # 8       deq
        deq = deque() # O(N) - space
        deq.append(nums[0])
        for i in range(1, len(nums)): # O(N) - time
            if deq[-1] == nums[i]:
                deq[-1] <<= 1
                while len(deq) > 1 and deq[-1] == deq[-2]:
                    deq.pop()
                    deq[-1] <<= 1
            else:
                deq.append(nums[i])
        return list(deq)