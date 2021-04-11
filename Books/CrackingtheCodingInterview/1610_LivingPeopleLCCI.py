"""
给定 N 个人的出生年份和死亡年份，第 i 个人的出生年份为 birth[i]，死亡年份为 death[i]，实现一个方法以计算生存人数最多的年份。

你可以假设所有人都出生于 1900 年至 2000 年（含 1900 和 2000 ）之间。如果一个人在某一年的任意时期处于生存状态，那么他应该被纳入那一年的统计中。例如，生于 1908 年、死于 1909 年的人应当被列入 1908 年和 1909 年的计数。

如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。

 

示例：

输入：
birth = {1900, 1901, 1950}
death = {1948, 1951, 2000}
输出： 1901
 

提示：

0 < birth.length == death.length <= 10000
birth[i] <= death[i]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/living-people-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        events = sorted([(b, 1) for b in birth] + [(d + 1, -1) for d in death])
        tmp, max_count = 0, 0
        res = None
        for year, flag in events:
            tmp += flag
            if tmp > max_count:
                max_count = tmp
                res = year
        return res

S = Solution()
birth = [1900, 1901, 1950]
death = [1948, 1951, 2000]
print(S.maxAliveYear(birth, death))