class Solution:
    def getSecondLargest(self, arr):
        largest = second_largest = -1

        for num in arr:
            if num > largest: 
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
              second_largest = num

        return second_largest
