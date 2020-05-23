"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        copy_arr = arr[:]
        zeros = 0
        index = 0
        c_index = 0
        len_arr = len(arr)
        while index < len(arr):
            arr[index] = copy_arr[c_index]
            if copy_arr[c_index] == 0:
                index += 1
                if index < len_arr:
                    arr[index] = 0
            c_index += 1
            index += 1


s = Solution()
arr = [1,0,2,3,0,4,5,0]
print(s.duplicateZeros(arr))

arr = [1,2,3]
print(s.duplicateZeros(arr))

arr = [0]
print(s.duplicateZeros(arr))