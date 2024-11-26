def circularSubarraySum(arr):
    def kadane(array):
        max_ending_here = max_so_far = array[0]
        for x in array[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    # Step 1: Maximum sum for non-circular subarray
    max_kadane = kadane(arr)
    # Step 2: Calculate total sum and invert elements for circular computation
    total_sum = sum(arr)
    arr_inverted = [-x for x in arr]
    # Step 3: Minimum subarray sum is the negative of maximum subarray sum of inverted array
    max_inverted_kadane = kadane(arr_inverted)
    max_circular = total_sum + max_inverted_kadane  # total_sum - (-min_subarray_sum)
    # Step 4: Handle edge case where all elements are negative
    if max_circular == 0:  # If all elements are negative, max_circular will be zero
        return max_kadane
    # Step 5: Return the maximum of circular and non-circular sums
    return max(max_kadane, max_circular)
