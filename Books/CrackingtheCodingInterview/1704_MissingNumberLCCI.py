"""
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？

注意：本题相对书上原题稍作改动

示例 1：

输入：[3,0,1]
输出：2
 

示例 2：

输入：[9,6,4,2,3,5,7,0,1]
输出：8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (1 + n) // 2 - sum(nums)

S = Solution()
nums = [3,0,1]
print(S.missingNumber(nums))
nums = [9,6,4,2,3,5,7,0,1]
print(S.missingNumber(nums))