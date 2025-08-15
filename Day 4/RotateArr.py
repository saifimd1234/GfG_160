class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        
        # Reverse first d elements
        self.reverse(arr, 0, d-1)
        # Reverse remaining elements
        self.reverse(arr, d, n-1)
        # Reverse entire array
        self.reverse(arr, 0, n-1)
    
    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = [1, 2, 3, 4, 5]
Solution().rotateArr(arr, 3)
print(arr)  # [3, 4, 5, 1, 2]
