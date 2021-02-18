"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-ii-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from itertools import permutations
from typing import List
class Solution:
    def permutation(self, string: str) -> List[str]:
        list_string = list(string)
        res = set()
        for perm in permutations(list_string):
            res.add(''.join(perm))
        return list(res)

from itertools import combinations
from typing import List
class Solution:
    def permutation(self, string: str) -> List[str]:
        list_string = list(string)
        repeats = len(list_string)
        res = []
        for comb in combinations(list_string, repeats):
            res.append(''.join(comb))
        return res

S = Solution()
print(S.permutation('qqe'))
print(S.permutation('ab'))