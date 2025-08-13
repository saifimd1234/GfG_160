# Reverse the array in place
# Time Complexity: O(n)
# Space Complexity: O(1)

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

arr = [1, 2, 3, 4, 5]
print(Solution().reverseArray(arr))  
# Output: [5, 4, 3, 2, 1]
