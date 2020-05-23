"""
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
"""
from bisect import bisect_left
class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr = sorted(arr)
        ava_target = target/len(arr)
        index = bisect_left(arr, ava_target)
        min_diff = float('inf')
        res = None
        print(target/len(arr))
        if index > 0:
            left = [arr[index-1]]
        else:
            left = [int(ava_target), int(ava_target)+1]
        if abs(sum(arr[], arr[]) - target) < min_diff:
            rse = left
        if index < len(arr):
            right = [arr[index]]
        else:
            right = [arr[index-1]]
        vals = left + right
        for v in vals:
            sums = 


s = Solution()
arr = [4,9,3]
target = 10
print(s.findBestValue(arr,target))
arr = [2,3,5]
target = 10
print(s.findBestValue(arr,target))
arr = [60864,25176,27249,21296,20204]
target = 56803
print(s.findBestValue(arr,target))
