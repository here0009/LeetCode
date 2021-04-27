"""
There is a garden of n flowers, and each flower has an integer beauty value. The flowers are arranged in a line. You are given an integer array flowers of size n and each flowers[i] represents the beauty of the ith flower.

A garden is valid if it meets these conditions:

The garden has at least two flowers.
The first and the last flower of the garden have the same beauty value.
As the appointed gardener, you have the ability to remove any (possibly none) flowers from the garden. You want to remove flowers in a way that makes the remaining garden valid. The beauty of the garden is the sum of the beauty of all the remaining flowers.

Return the maximum possible beauty of some valid garden after you have removed any (possibly none) flowers.

 

Example 1:

Input: flowers = [1,2,3,1,2]
Output: 8
Explanation: You can produce the valid garden [2,3,1,2] to have a total beauty of 2 + 3 + 1 + 2 = 8.
Example 2:

Input: flowers = [100,1,1,-3,1]
Output: 3
Explanation: You can produce the valid garden [1,1,1] to have a total beauty of 1 + 1 + 1 = 3.
Example 3:

Input: flowers = [-1,-2,0,-1]
Output: -2
Explanation: You can produce the valid garden [-1,-1] to have a total beauty of -1 + -1 = -2.
 

Constraints:

2 <= flowers.length <= 105
-104 <= flowers[i] <= 104
It is possible to create a valid garden by removing some (possibly none) flowers.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-the-beauty-of-the-garden
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:

        total = 0
        length = len(flowers)
        max_value = [0] * length
        for i, v in enumerate(flowers):
            if v > 0:
                total += v
            max_value[i] = total
        flower_idx = dict()
        res = -float('inf')
        for i, v in enumerate(flowers):
            if v in flower_idx:
                tmp = max_value[i] - max_value[flower_idx[v]] + 2 * v
                if v > 0:  # max_value[i] including v
                    tmp -= v
                res = max(res, tmp)
            else:
                flower_idx[v] = i
        # print(flower_idx)
        # print(max_value)
        return res if res != -float('inf') else None


S = Solution()
flowers = [1,2,3,1,2]
print(S.maximumBeauty(flowers))
flowers = [100,1,1,-3,1]
print(S.maximumBeauty(flowers))
flowers = [-1,-2,0,-1]
print(S.maximumBeauty(flowers))