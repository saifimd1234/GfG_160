Your code for reversing the array **in-place** looks correct — it’s using the **two-pointer approach** efficiently.

Here’s what’s happening step-by-step:

---

### **Code (Clean Version)**

```python
class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            # Swap elements at left and right
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
```

---

### **Example Run**

```python
arr = [1, 2, 3, 4, 5]
print(Solution().reverseArray(arr))  
# Output: [5, 4, 3, 2, 1]
```

---

✅ **Why it works:**

* **Two pointers** (`left` and `right`) start from opposite ends.
* Swap values at these positions.
* Move `left` forward and `right` backward until they meet or cross.
* No extra space used → **O(1) space**.
* Runs in **O(n) time**.

---
