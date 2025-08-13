I see why your code isn’t working — the issue is in this part:

```python
[0] + newArr
```

This **creates a new list** with `0` at the front but **doesn’t assign it anywhere**, so it’s ignored. Also, the logic is reversed — you want zeros at the **end**, not the start.

---

### **Correct O(n) Solution**

```python
class Solution:
    def pushZerosToEnd(self, arr):
        # List to store non-zero elements
        newArr = []
        
        zero_count = 0  # Count how many zeros are in the array
        
        for num in arr:
            if num != 0:
                newArr.append(num)
            else:
                zero_count += 1
        
        # Append zeros at the end
        newArr.extend([0] * zero_count)
        
        return newArr
```

---

**Example:**

```python
print(Solution().pushZerosToEnd([0, 1, 0, 3, 12]))  
# Output: [1, 3, 12, 0, 0]
```

---

✅ **Why this works:**

* We **separate** non-zero numbers from zeros.
* Count zeros (`zero_count`).
* Add zeros at the end in one go using `.extend([0] * zero_count)`.

---

I see what’s going wrong — your logic is fine for **creating** a new list,
but the problem is you are **returning a new list** instead of **modifying the original `arr` in-place**.

The expected output `[3, 5, 4, 0, 0]` means the test case is checking the same `arr` after the function runs, not your returned value.

---

### **In-place Two-Pointer Solution (O(n) time, O(1) space)**

```python
class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        pos = 0  # Position to place the next non-zero
        
        # Move non-zero numbers forward
        for i in range(n):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # Fill the remaining positions with zeros
        while pos < n:
            arr[pos] = 0
            pos += 1
```

---

**Example:**

```python
arr = [3, 0, 5, 0, 4]
Solution().pushZerosToEnd(arr)
print(arr)  # [3, 5, 4, 0, 0]
```

---

✅ **Why this works:**

* **`pos`** keeps track of where the next non-zero should go.
* First loop moves all non-zeros forward.
* Second loop fills remaining positions with `0`.
* This way, we **don’t create a new list** and we **modify `arr` in-place**.

---

Here’s the **two-pointer in-place method** for moving all zeros to the end while keeping the order of non-zero elements:

---

### **Two-Pointer In-Place Approach**

```python
class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        left = 0  # Pointer for placing the next non-zero element
        
        # Traverse with right pointer
        for right in range(n):
            if arr[right] != 0:
                # Swap non-zero element with left pointer position
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
```

---

**Example usage:**

```python
arr = [3, 0, 5, 0, 4]
Solution().pushZerosToEnd(arr)
print(arr)  # [3, 5, 4, 0, 0]
```

---

**How it works step-by-step:**

1. **`left`** keeps track of the position to put the next non-zero number.
2. **`right`** scans through the list.
3. When a non-zero is found:

   * Swap it with the element at `left`.
   * Increment `left` so it’s ready for the next non-zero.
4. Zeros naturally get pushed to the end.

⏳ **Time complexity:** O(n)
📦 **Space complexity:** O(1) (no extra list created)

---
