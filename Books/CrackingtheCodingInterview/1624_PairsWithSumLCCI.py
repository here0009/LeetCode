"""
设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。

示例 1:

输入: nums = [5,6,5], target = 11
输出: [[5,6]]
示例 2:

输入: nums = [5,6,5,6], target = 11
输出: [[5,6],[5,6]]
提示：

nums.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pairs-with-sum-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import Counter
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        counts = Counter(nums)
        res = []
        visited = set()
        for k, v in counts.items():
            k2 = target - k
            if k in visited or k2 in visited or k2 not in counts:
                continue
            if k == k2:
                min_v = v // 2
            else:
                min_v = min(v, counts[k2])
            res.extend([[k, k2] for _ in range(min_v)])
            visited |= {k, k2}
        return res

S = Solution()
nums = [5,6,5]
target = 11
print(S.pairSums(nums, target))

nums = [5,6,5,6]
target = 11
print(S.pairSums(nums, target))
            
nums = [-2,-1,0,3,5,6,7,9,13,14]
target = 12
print(S.pairSums(nums, target))

