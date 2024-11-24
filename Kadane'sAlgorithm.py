class Solution:
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize variables
        max_current = arr[0]  # Maximum sum of the subarray ending here
        max_global = arr[0]   # Maximum sum of any subarray so far

        for i in range(1, len(arr)):
            # Update max_current to include the current element or start fresh from the current element
            max_current = max(arr[i], max_current + arr[i])
            
            # Update max_global if max_current is greater
            if max_current > max_global:
                max_global = max_current

        return max_global
