"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        """
        wrong answer for test case
        first = "ab"
        second = "bc"
        """
        f_len, s_len = len(first), len(second)
        if abs(f_len - s_len) > 1:
            return False
        dp = [[0] * (s_len + 1) for _ in range(f_len + 1)]
        for i in range(1, f_len + 1):
            for j in range(1, s_len + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + int(first[i - 1] == second[j - 1]))
        for row in dp:
            print(row)
        return dp[-1][-1] >= max(f_len, s_len) - 1


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        f_len, s_len = len(first), len(second)
        if s_len < f_len:
            first, second = second, first
            f_len, s_len = s_len, f_len
        if f_len - s_len > 1:
            return False
        equal = int(f_len == s_len)
        mismatch = 0
        i = 0
        j = 0
        while i < f_len:
            while j < s_len and second[j] != first[i]:
                j += 1
                i += equal
                mismatch += 1
            if j == s_len or mismatch > 1:
                break
            i += 1
            j += 1
        while j < s_len:
            j += 1
            mismatch += 1
        # print(first, second, i, j, mismatch)
        return i == f_len and mismatch <= 1

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        f_len, s_len = len(first), len(second)
        if s_len < f_len:
            first, second = second, first
            f_len, s_len = s_len, f_len
        if f_len - s_len > 1:
            return False
        equal = int(f_len == s_len)
        mismatch = 0
        i = 0
        j = 0
        while i < f_len and j < s_len:
            if second[j] != first[i]:
                i += equal
                mismatch += 1
            else:
                i += 1
            j += 1
        while i < f_len:
            i += 1
            mismatch += 1
        while j < s_len:
            j += 1
            mismatch += 1
        return mismatch <= 1


S = Solution()
first = "pale"
second = "ple"
print(S.oneEditAway(first, second))
first = "pales"
second = "pal"
print(S.oneEditAway(first, second))
first = "ab"
second = "bc"
print(S.oneEditAway(first, second))
first = ""
second = "a"
print(S.oneEditAway(first, second))
first = "a"
second = "ab"
print(S.oneEditAway(first, second))
first = "teacher"
second ="beacher"
print(S.oneEditAway(first, second))
