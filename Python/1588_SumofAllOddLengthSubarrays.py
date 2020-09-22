"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3res
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""


class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        res = 0
        length = len(arr)
        preSum, tmp = [0], 0
        for i in range(length):
            tmp += arr[i]
            preSum.append(tmp)
        for l in range(1, length+1, 2):
            for i in range(0, length-l+1):
                res += preSum[i+l] - preSum[i]
        return res

class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        res, n = 0, len(arr)
        for i in range(n):
            res += ((i + 1) * (n - i) + 1) // 2 * arr[i]
            # print(i+1, n-i)
        return res

S = Solution()
arr = [1,4,2,5,3]
print(S.sumOddLengthSubarrays(arr))
arr = [1,2]
print(S.sumOddLengthSubarrays(arr))
arr = [10,11,12]
print(S.sumOddLengthSubarrays(arr))