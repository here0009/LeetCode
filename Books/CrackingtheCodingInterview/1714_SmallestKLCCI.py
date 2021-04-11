"""
Design an algorithm to find the smallest K numbers in an array.

Example:

Input:  arr = [1,3,5,7,2,4,6,8], k = 4
Output:  [1,2,3,4]
Note:

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-k-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]

import heapq
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        res = []
        while k > 0:
            res.append(heapq.heappop(arr))
            k -= 1
        return res