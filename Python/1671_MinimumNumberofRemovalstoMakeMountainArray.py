"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
Example 3:

Input: nums = [4,3,2,1,1,2,3,1]
Output: 4
Example 4:

Input: nums = [1,2,3,4,4,3,2,1]
Output: 1
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
"""


from typing import List
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        calculate the max length of increasing list from start for each index.
        max length of increasing list from end for each index
        then combine the result
        """
        length = len(nums)
        left = [0]*length
        right = [0]*length

        for i in range(length):
            tmp = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp = max(tmp, 1+left[j])
            left[i] = tmp

        for i in range(length-1, -1, -1):
            tmp = 1
            for j in range(length-1, i, -1):
                if nums[j] < nums[i]:
                    tmp = max(tmp, 1+right[j])
            right[i] = tmp
        res = 0
        for i in range(1, length-1):
            res = max(res, left[i]+right[i]-1)
        # print('+++++++')
        # print(length)
        # print(nums)
        # print(left)
        # print(right)
        return length - res


from typing import List
from bisect import bisect_left
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        length = len(nums)
        left = [0]*length
        right = [0]*length

        stack = []
        for i in range(length):
            k = bisect_left(stack, nums[i])
            left[i] = k+1
            if k == len(stack):
                stack.append(nums[i])
            else:
                stack[k] = nums[i]

        stack = []
        for i in range(length-1, -1, -1):
            k = bisect_left(stack, nums[i])
            right[i] = k+1
            if k == len(stack):
                stack.append(nums[i])
            else:
                stack[k] = nums[i]

        res = 0
        for i in range(1, length-1):
            res = max(res, left[i]+right[i]-1)

        return length - res


class Solution:   
    def minimumMountainRemovals(self, A):
        n = len(A)
        dp = [0] * n
        mono = [float('inf')] * n
        for i in range(n):
            j = bisect_left(mono, A[i])
            mono[j] = A[i]
            dp[i] += j + 1
        mono = [float('inf')] * n
        for i in range(n - 1, -1, -1):
            j = bisect_left(mono, A[i])
            mono[j] = A[i]
            dp[i] += j
        return n - max(dp[1:-1])


S = Solution()
nums = [1,3,1]
print(S.minimumMountainRemovals(nums))
nums = [2,1,1,5,6,2,3,1]
print(S.minimumMountainRemovals(nums))
nums = [4,3,2,1,1,2,3,1]
print(S.minimumMountainRemovals(nums))
nums = [1,2,3,4,4,3,2,1]
print(S.minimumMountainRemovals(nums))
nums = [23,47,63,72,81,99,88,55,21,33,32]
print(S.minimumMountainRemovals(nums))
