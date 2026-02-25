class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, item):
        """Insert item into PQ"""
        self.data.append(item)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        """Remove and return smallest item"""
        if not self.data:
            raise IndexError("pop from empty priority queue")

        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._sift_down(0)
        return item

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent] <= self.data[i]:
                break
            self._swap(i, parent)
            i = parent

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __len__(self):
        return len(self.data)


class DAryHeap:
    def __init__(self, d=4):
        self.d = d
        self.data = []

    def push(self, x):
        self.data.append(x)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self.data) - 1)
        x = self.data.pop()
        self._sift_down(0)
        return x

    def _sift_up(self, i):
        parent = (i - 1) // self.d
        while i > 0 and self.data[i] < self.data[parent]:
            self._swap(i, parent)
            i = parent
            parent = (i - 1) // self.d

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            smallest = i
            for k in range(1, self.d + 1):
                child = self.d * i + k
                if child < n and self.data[child] < self.data[smallest]:
                    smallest = child
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __len__(self):
        return len(self.data)


pq = PriorityQueue()
pq.push(5)
pq.push(1)
pq.push(3)

print(pq.pop())  # 1
print(pq.pop())  # 3
print(pq.pop())  # 5

pq = DAryHeap(d=4)
pq.push((3, "a"))
pq.push((1, "b"))
pq.push((2, "c"))

print(pq.pop())  # (1, "b")

