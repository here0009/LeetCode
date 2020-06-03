"""
Given an array of integers arr and two integers k and threshold.

Return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [1,1,1,1,1], k = 1, threshold = 0
Output: 5
Example 3:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
Example 4:

Input: arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
Output: 1
Example 5:

Input: arr = [4,4,4,4], k = 4, threshold = 1
Output: 1
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^4
1 <= k <= arr.length
0 <= threshold <= 10^4
"""


class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        i = 0
        length = len(arr)
        tmp = sum(arr[:k])
        res = 0
        threshold = threshold * k
        res += (tmp >= threshold)
        while i + k < length:
            tmp = tmp - arr[i] + arr[i+k]
            res += (tmp >= threshold)
            i += 1
        return res

S = Solution()
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(S.numOfSubarrays(arr, k, threshold))
arr = [1,1,1,1,1]
k = 1
threshold = 0
print(S.numOfSubarrays(arr, k, threshold))
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(S.numOfSubarrays(arr, k, threshold))
arr = [7,7,7,7,7,7,7]
k = 7
threshold = 7
print(S.numOfSubarrays(arr, k, threshold))
arr = [4,4,4,4]
k = 4
threshold = 1
print(S.numOfSubarrays(arr, k, threshold))
