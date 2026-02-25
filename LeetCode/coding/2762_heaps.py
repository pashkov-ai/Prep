from dataclasses import dataclass, field
import heapq
from typing import Any, Protocol, TypeVar

T = TypeVar("T")

class NegatableComparable(Protocol):
    def __neg__(self: T) -> T:
        ...
    
    def __lt__(self, other: T) -> bool:
        ...

@dataclass(order=True)
class ValueIndex(NegatableComparable):
    index: int = field(compare=False)
    value: int
    
    def __neg__(self):
        return ValueIndex(self.index, -self.value)

class Heap:

    def __init__(self, typee: str):
        if typee not in {'min', 'max'}:
            raise ValueError('type must be either "min" or "max"')
        self.heap = list()
        self.type = typee

    def __len__(self) -> int:
        return len(self.heap)

    def push(self, x: NegatableComparable) -> None:
        if self.type == 'min':
            heapq.heappush(self.heap, x)
        elif self.type == 'max':
            heapq.heappush(self.heap, -x)

    def pop(self) -> Any:
        if self.type == 'min':
            return heapq.heappop(self.heap)
        elif self.type == 'max':
            return -heapq.heappop(self.heap)

    def peek(self) -> Any:
        if self.type == 'min':
            return self.heap[0]
        elif self.type == 'max':
            return -self.heap[0]


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        minheap = Heap('min')
        maxheap = Heap('max')

        left = right = 0
        counter = 0
        while right < len(nums):
            # update heaps
            minheap.push(ValueIndex(right, nums[right]))
            maxheap.push(ValueIndex(right, nums[right]))
            # while window is invalid (invariant)
            while left < right and maxheap.peek().value - minheap.peek().value > 2:
                left += 1
                while minheap and minheap.peek().index < left:
                    minheap.pop()
                while maxheap and maxheap.peek().index < left:
                    maxheap.pop()
            # add subarray count for current valid window
            counter += right - left + 1
            # move right
            right += 1
        return counter