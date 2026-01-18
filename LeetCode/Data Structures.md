📚 Stack (LIFO: Last In, First Out)  
list with append()/pop()
✅ Interface:  
    push(x)	Add element x to the top  
    pop()	Remove and return the top element  
    peek() / top()	Return the top element without removing it  
    is_empty()	Check if stack is empty  
    size()	Number of elements in the stack  

🚦 Queue (FIFO: First In, First Out)
collections.deque with append()/popleft()
✅ Interface:
    enqueue(x)	Add element x to the end (tail)
    dequeue()	Remove and return the front element
    peek() / front()	Return the front element without removing
    is_empty()	Check if queue is empty
    size()	Number of elements in the queue


## 🧩 Generic Deque API with Python Equivalents

| **Generic Deque API**    | **Description**                                     | **Python `collections.deque` Equivalent** | **Python `list` Equivalent**         | **Time Complexity** |
| ------------------------ | --------------------------------------------------- | ----------------------------------------- | ------------------------------------ | ------------------- |
| `append_left(item)`      | Add an element to the **front** of the deque        | `deque.appendleft(item)`                  | `list.insert(0, item)`               | `O(1)` / `O(n)`     |
| `append_right(item)`     | Add an element to the **back** of the deque         | `deque.append(item)`                      | `list.append(item)`                  | `O(1)`              |
| `pop_left()`             | Remove and return element from the **front**        | `deque.popleft()`                         | `list.pop(0)`                        | `O(1)` / `O(n)`     |
| `pop_right()`            | Remove and return element from the **back**         | `deque.pop()`                             | `list.pop()`                         | `O(1)`              |
| `peek_left()`            | Return the **front** element without removing it    | `deque[0]`                                | `list[0]`                            | `O(1)`              |
| `peek_right()`           | Return the **rear** element without removing it     | `deque[-1]`                               | `list[-1]`                           | `O(1)`              |
| `is_empty()`             | Check if deque is empty                             | `len(deque) == 0`                         | `len(list) == 0`                     | `O(1)`              |
| `clear()`                | Remove all elements                                 | `deque.clear()`                           | `list.clear()`                       | `O(1)`              |
| `__len__()`              | Return number of elements                           | `len(deque)`                              | `len(list)`                          | `O(1)`              |
| `__iter__()`             | Iterate from front to back                          | `for x in deque:`                         | `for x in list:`                     | `O(n)`              |
| `__reversed__()`         | Iterate from back to front                          | `for x in reversed(deque):`               | `for x in reversed(list):`           | `O(n)`              |
| `extend_left(iterable)`  | Add multiple items to the **front**                 | `deque.extendleft(iterable)`              | `[x for x in iterable[::-1]] + list` | `O(k)` / `O(n+k)`   |
| `extend_right(iterable)` | Add multiple items to the **back**                  | `deque.extend(iterable)`                  | `list.extend(iterable)`              | `O(k)`              |
| `rotate(n)`              | Rotate elements n steps right (or left if negative) | `deque.rotate(n)`                         | `lst[:] = lst[-n:] + lst[:-n]`       | `O(n)`              |

---

Queue
q = deque()
q.append('a')       # enqueue
q.append('b')
print(q.popleft())  # dequeue → 'a'

Stack
s = deque()
s.append('x')       # push
s.append('y')
print(s.pop())      # pop → 'y'

Fixed-Size Sliding Window
dq = deque(maxlen=3)
dq.extend([1, 2, 3])
dq.append(4)        # 1 is dropped → dq: [2, 3, 4]

Rotate
dq = deque([1, 2, 3])
dq.rotate(1)        # dq → [3, 1, 2]
dq.rotate(-1)       # dq → [1, 2, 3]


| Function                        | Description                                |
| ------------------------------- | ------------------------------------------ |
| `heapq.heapify(lst)`            | Convert list into a heap, in-place (O(n))  |
| `heapq.heappush(heap, item)`    | Add item to heap (O(log n))                |
| `heapq.heappop(heap)`           | Remove and return smallest item (O(log n)) |
| `heapq.heappushpop(heap, item)` | Push then pop in one step (faster)         |
| `heapq.heapreplace(heap, item)` | Pop then push (always removes smallest)    |
| `heapq.nlargest(n, iterable)`   | Return n largest elements (heap-backed)    |
| `heapq.nsmallest(n, iterable)`  | Return n smallest elements                 |
