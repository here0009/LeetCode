"""
You are given an array target that consists of distinct integers and another integer array arr that can have duplicates.

In one operation, you can insert any integer at any position in arr. For example, if arr = [1,4,1,2], you can add 3 in the middle and make it [1,4,3,1,2]. Note that you can insert the integer at the very beginning or end of the array.

Return the minimum number of operations needed to make target a subsequence of arr.

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

 

Example 1:

Input: target = [5,1,3], arr = [9,4,2,3,4]
Output: 2
Explanation: You can add 5 and 1 in such a way that makes arr = [5,9,4,1,2,3,4], then target will be a subsequence of arr.
Example 2:

Input: target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
Output: 3
 

Constraints:

1 <= target.length, arr.length <= 105
1 <= target[i], arr[i] <= 109
target contains no duplicates.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from bisect import bisect_left
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """
        Thoughts: find the longest increasing subsequence of target in arr
        then len(target) - len(LIS)
        """
        v_i = {v: i for i, v in enumerate(target)}
        LIS = []
        for num in arr:
            if num in v_i:
                idx = v_i[num]
                j = bisect_left(LIS, idx)
                if j == len(LIS):
                    LIS.append(idx)
                else:
                    LIS[j] = idx
                # print([target[i] for i in LIS])
        return len(target) - len(LIS)

S = Solution()
target = [5,1,3]
arr = [9,4,2,3,4]
print(S.minOperations(target, arr))
target = [6,4,8,1,3,2]
arr = [4,7,6,2,3,8,6,1]
print(S.minOperations(target, arr))