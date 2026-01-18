Excellent — you want a **generic Deque API** that’s **implementation-agnostic** (as if you were designing a cross-language or abstract interface), **but mapped to Python equivalents** using both:

* `collections.deque` (for efficient O(1) operations on both ends)
* `list` (for educational or compatibility purposes, though some operations are O(n))

Here’s a clear, structured reference 👇

---

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

## 🧱 Example: Generic Deque Wrapper

Here’s a generic class that can switch between **`deque`** and **`list`** as the underlying implementation:

```python
from collections import deque

class GenericDeque:
    """A generic Deque API with interchangeable backend (deque or list)."""

    def __init__(self, iterable=None, backend="deque"):
        self.backend = backend
        if backend == "deque":
            self._data = deque(iterable or [])
        elif backend == "list":
            self._data = list(iterable or [])
        else:
            raise ValueError("Backend must be either 'deque' or 'list'")

    # Core Operations
    def append_left(self, item):
        if self.backend == "deque":
            self._data.appendleft(item)
        else:
            self._data.insert(0, item)

    def append_right(self, item):
        self._data.append(item)

    def pop_left(self):
        if self.is_empty():
            raise IndexError("pop_left from empty deque")
        return self._data.popleft() if self.backend == "deque" else self._data.pop(0)

    def pop_right(self):
        if self.is_empty():
            raise IndexError("pop_right from empty deque")
        return self._data.pop()

    # Peek Operations
    def peek_left(self):
        if self.is_empty():
            raise IndexError("peek_left from empty deque")
        return self._data[0]

    def peek_right(self):
        if self.is_empty():
            raise IndexError("peek_right from empty deque")
        return self._data[-1]

    # Utilities
    def clear(self):
        self._data.clear()

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __reversed__(self):
        return reversed(self._data)

    def __repr__(self):
        return f"GenericDeque({list(self._data)}, backend='{self.backend}')"
```

---

## ⚙️ Example Usage

```python
dq = GenericDeque([1, 2, 3], backend="deque")
dq.append_left(0)
dq.append_right(4)
print(dq)  # GenericDeque([0, 1, 2, 3, 4], backend='deque')

print(dq.pop_left())   # 0
print(dq.pop_right())  # 4
print(dq.peek_left())  # 1
print(dq.peek_right()) # 3

# Switch backend to list
lst_dq = GenericDeque([1, 2, 3], backend="list")
lst_dq.append_left(0)
lst_dq.append_right(4)
print(lst_dq)  # GenericDeque([0, 1, 2, 3, 4], backend='list')
```

---

Would you like me to extend this to include **thread-safe** versions (using `queue` or locks), or just keep it as a lightweight generic API?
