class Solution:
    def getSecondLargest(self, arr):
        # Remove duplicates
        unique_arr = list(set(arr))
        
        # If less than 2 unique elements, second largest doesn't exist
        if len(unique_arr) < 2:
            print(-1)
        
        # Sort and return second last element
        else:
            unique_arr.sort()
            print(unique_arr[-2])


Solution().getSecondLargest([10, 20, 4, 45, 99])  # Output: 45
Solution().getSecondLargest([10, 10, 10])        # Output: -1
Solution().getSecondLargest([10, 10, 5])         # Output: 5
