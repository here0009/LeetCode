"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
"""
class Solution_1:
    def findClosestElements(self, arr, k: int, x: int):
        len_arr = len(arr)
        arr_x = [(abs(arr[i]-x),i) for i in range(len_arr)]
        arr_x = sorted(arr_x)
        return sorted([arr[i] for _,i in arr_x[:k]])

from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        index = bisect_left(arr, x)
        left = max(0, index-k) #k numbers befor index, because arr[index] may be not in the final resutlt
        right = min(len(arr)-1, index+k)
        while right-left > k-1:
            if x - arr[left] > arr[right] - x:
                left += 1
            else:
                right -= 1
        return arr[left:right+1]

s = Solution()
arr = [1,2,3,4,5]
k = 4
x = 3
print(s.findClosestElements(arr, k, x))

arr = [1,2,3,4,5]
k=4
x=-1
print(s.findClosestElements(arr, k, x))
