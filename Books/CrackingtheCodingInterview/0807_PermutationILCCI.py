"""
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-i-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from itertools import permutations as perm
class Solution:
    def permutation(self, string: str) -> List[str]:
        res = []
        for p in perm(list(string)):
            res.append(''.join(p))
        return res


class Solution:
    def permutation(self, string: str) -> List[str]:
        def dfs(i, tmp):
            if i == length:
                self.res.append(tmp)
            for j, v in enumerate(string):
                if visited[j] == 0:
                    visited[j] = 1
                    dfs(i + 1, tmp + v)
                    visited[j] = 0

        length = len(string)
        visited = [0] * length
        self.res = []
        dfs(0, '')
        return self.res

S = Solution()
print(S.permutation('qwe'))
print(S.permutation('ab'))