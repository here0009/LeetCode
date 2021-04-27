"""
给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

示例 1:

输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]

输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
示例 2:

输入: ["A","A"]

输出: []
提示：

array.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-longest-subarray-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:

        pos = dict()
        tmp = 0
        res = [0, 0]
        pos[0] = -1
        for i, v in enumerate(array):
            if v.isdigit():
                tmp += 1
            else:
                tmp -= 1
            if tmp not in pos:
                pos[tmp] = i
            else:
                if i - pos[tmp] > res[1] - res[0]:
                    res = [pos[tmp], i]
            # print(i, v, tmp, pos)
        if res[1] - res[0] == 0:
            return []
        # print(pos)
        return array[res[0] + 1: res[1] + 1]  # including right boundary, not including left boundary


S = Solution()
array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
print(S.findLongestSubarray(array))
array = ["A","A"]
print(S.findLongestSubarray(array))
array = ["A","1"]
print(S.findLongestSubarray(array))