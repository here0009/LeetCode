"""
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

 

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
 

Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4
"""
from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        res = defaultdict(int)
        # for a in arr:
        #     if difference == 0:
        #         res[a] = res.get(a,0) + 1
        #     else:
        #         if a - difference in res:
        #             res[a] = res[a - difference] + 1
        #             res.pop(a - difference)
        #         else:
        #             res[a] = 1
        for a in arr:
            res[a] = max(res[a], res[a-difference]+1)
        # print(res)
        return max(res.values())

s = Solution()
arr = [1,2,3,4]
difference = 1
print(s.longestSubsequence(arr, difference))

arr = [1,3,5,7]
difference = 1
print(s.longestSubsequence(arr, difference))

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(s.longestSubsequence(arr, difference))

arr = [4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8]
difference = 0
# Output:
# 1
# Expected:
# 2
print(s.longestSubsequence(arr, difference))


arr = [7,-2,8,10,6,18,9,-8,-5,18,13,-6,-17,-1,-6,-9,9,9]
difference = 1
# Output:
# 2
# Expected:
# 3
print(s.longestSubsequence(arr, difference))