"""
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
Example 4:

Input: arr = [1]
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        """
        find the longest sorted subarray
        wrong answer, we should remove a continouse subarray
        """
        length_dict = {-1:0}
        for num in arr:
            value = max(v for k,v in length_dict.items() if k <= num) + 1
            length_dict[num] = value
        print(len(arr))
        print(arr)
        print(length_dict)
        return len(arr) - max(length_dict.values())


class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        """
        wrong answer,can not use stack to pop left values
        """
        length = len(arr)
        # print('arr' ,arr)
        if length == 1:
            return 0
        left, right = 1, length-1
        while left < length and arr[left] >= arr[left-1]:
            left += 1
        if left == length:
            return 0
        # arr[:left] is sorted
        while right > 0 and arr[right] >= arr[right-1]:
            right -= 1
        # arr[right:] is sorted
        if arr[left-1] <= arr[right] and left <= right:
            return right-left
        res = min(length-left, right)
        left_arr = arr[:left]
        print(left, right, length)
        print(arr[:left])
        print(arr[right:])
        while right <= length-1:
            while left_arr and left_arr[-1] > arr[right]:
                left_arr.pop()
            print(arr[right], left_arr)
            res = min(res, right - len(left_arr))
            right += 1
        return res

from bisect import bisect_right
class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        length = len(arr)
        # print('arr' ,arr)
        if length == 1:
            return 0
        left, right = 1, length-1
        while left < length and arr[left] >= arr[left-1]:
            left += 1
        if left == length:
            return 0
        # arr[:left] is sorted
        while right > 0 and arr[right] >= arr[right-1]:
            right -= 1
        # arr[right:] is sorted
        if arr[left-1] <= arr[right] and left <= right:
            return right-left
        res = min(length-left, right)  # remove left or right part of ther arrays
        left_arr = arr[:left]
        while right <= length-1:
            index = bisect_right(left_arr, arr[right])
            # print(left_arr, arr[right], index)
            res = min(res, right-index) #half include(index) and half not include(right), so the length is right-index
            right += 1
        return res




S = Solution()
# arr = [1,2,3,10,4,2,3,5]
# print(S.findLengthOfShortestSubarray(arr))
# arr = [5,4,3,2,1]
# print(S.findLengthOfShortestSubarray(arr))
# arr = [1,2,3]
# print(S.findLengthOfShortestSubarray(arr))
# arr = [1]
# print(S.findLengthOfShortestSubarray(arr))
# arr = [13,0,14,7,18,18,18,16,8,15,20]
# print(S.findLengthOfShortestSubarray(arr))
# Output
# 5
# Expected
# 8
arr = [10,13,17,21,15,15,9,17,22,22,13]
print(S.findLengthOfShortestSubarray(arr))
# Output
# 8
# Expected
# 7
arr = [1,2,3,10,0,7,8,9]
print(S.findLengthOfShortestSubarray(arr))
# Output
# 4
# Expected
# 2