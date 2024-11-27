class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Replace non-positive numbers and numbers greater than n with 0
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = 0
        
        # Step 2: Use the indices of the array to mark presence
        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
                # Mark the index val-1 as visited by making it negative
                if arr[val - 1] > 0:
                    arr[val - 1] = -arr[val - 1]
                elif arr[val - 1] == 0:
                    arr[val - 1] = -(n + 1)  # Use a special marker if the value was zero
        
        # Step 3: Find the first index that is non-negative
        for i in range(n):
            if arr[i] >= 0:
                return i + 1
        
        # If all indices are marked, return n+1
        return n + 1