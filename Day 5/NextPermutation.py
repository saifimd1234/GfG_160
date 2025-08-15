def next_permutation(nums):
    n = len(nums)
    
    # 1️⃣ Step 1: Find the first index 'i' from the end where nums[i] < nums[i+1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # 2️⃣ Step 2: If such index exists, find the first index 'j' from the end where nums[j] > nums[i]
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # 3️⃣ Step 3: Reverse the subarray nums[i+1:]
    nums[i + 1:] = reversed(nums[i + 1:])


# Example usage:
arr = [1, 3, 2]
next_permutation(arr)
print(arr)  # Output: [2, 1, 3]
