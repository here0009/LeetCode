"""
Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
Example 4:

Input: arr = [5,5,4,4,5], target = 3
Output: -1
Explanation: We cannot find a sub-array of sum = 3.
Example 5:

Input: arr = [3,1,1,1,5,1,2,1], target = 3
Output: 3
Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
"""


from collections import deque
class Solution:
    def minSumOfLengths(self, arr, target: int) -> int:
        """
        TLE
        """
        dq = deque([])
        tmp = 0
        pos_list = []
        for i, v in enumerate(arr):
            dq.append((i,v))
            tmp += v
            while tmp >= target:
                if tmp == target:
                    pos_list.append((dq[0][0], dq[-1][0]))
                tmp -= dq.popleft()[1]
            # print(dq)
        # print(pos_list)
        # pos_list = sorted(pos_list, key=lambda x:x[1]-x[0])
        length = len(pos_list)
        res = float('inf')
        for i in range(length-1):
            for j in range(i+1, length):
                si,ei = pos_list[i]
                sj,ej = pos_list[j]
                if ei < sj or ej < si:
                    res = min(res, ei-si+ej-sj+2)
        return res if res != float('inf') else -1


class Solution:
    def minSumOfLengths(self, arr, target: int) -> int:
        curr = 0
        left = 0
        res = float('inf')
        dp = [float('inf')]*(len(arr)+1)
        for right, v in enumerate(arr):
            curr += v
            while curr > target and left <= right:
                curr -= arr[left]
                left += 1
            if curr == target:
                dp[right] = min(dp[right-1], right-left+1)
                res = min(res, dp[left-1]+right-left+1) #dp[-1] was set to be inf, so its ok if left is 0
            else:
                dp[right] = dp[right-1]
        return res if res != float('inf') else -1


S = Solution()
arr = [3,2,2,4,3]
target = 3
print(S.minSumOfLengths(arr, target))
arr = [7,3,4,7]
target = 7
print(S.minSumOfLengths(arr, target))
arr = [4,3,2,6,2,3,4]
target = 6
print(S.minSumOfLengths(arr, target))
arr = [5,5,4,4,5]
target = 3
print(S.minSumOfLengths(arr, target))
arr = [3,1,1,1,5,1,2,1]
target = 3
print(S.minSumOfLengths(arr, target))