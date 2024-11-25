class Solution:
    def maxProduct(self, arr):
        # Initialize variables
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        # Traverse through the array starting from the second element
        for i in range(1, len(arr)):
            num = arr[i]
            
            # If the current number is negative, swap max and min
            if num < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product
            max_product = max(num, num * max_product)
            min_product = min(num, num * min_product)
            
            # Update the result
            result = max(result, max_product)
        
        return result
