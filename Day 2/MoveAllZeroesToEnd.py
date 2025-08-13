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

    def pushZerosToEndInPlace(self, arr):
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

        return arr

print(Solution().pushZerosToEnd([0, 1, 0, 3, 12]))  
print(Solution().pushZerosToEndInPlace([0, 1, 0, 3, 12]))
# Output: [1, 3, 12, 0, 0]
