"""
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-transforms-into-another-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
from collections import defaultdict
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        wrong answer
        """
        edges = defaultdict(set)
        indegree = defaultdict(set)
        for p, q in zip(str1, str2):
            edges[p].add(q)
            indegree[q].add(p)
        # print(edges, indegree)
        letters = set(edges.keys()) - set(indegree.keys())
        # print(letters)
        while letters:
            l2 = set()
            for c in letters:
                if len(edges[c]) > 1:
                    return False
                if not edges[c]:
                    continue
                # print(c, edges[c])
                d = edges[c].pop()
                indegree[d].remove(c)

                if len(indegree[d]) == 0:
                    l2.add(d)
            letters = l2
        # print(indegree)
        return all(len(indegree[d]) == 0 for d in indegree)


from collections import defaultdict
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        edges = defaultdict(set)
        indegree = defaultdict(set)
        for p, q in zip(str1, str2):
            edges[p].add(q)
            indegree[q].add(p)
            if len(edges[p]) > 1:
                return False
        if len(edges) < 26:
            return True
        if len(edges) == 26 and len(indegree) < 26:
            return True
        return False

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        m = dict()
        exists = set()
        for i in range(len(str1)):
            if str1[i] not in m:
                m[str1[i]] = str2[i]
                exists.add(str2[i])
            elif m[str1[i]] != str2[i]:
                return False
        return len(exists) < 26
"""
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/string-transforms-into-another-string/solution/zi-fu-chuan-zhuan-hua-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        out_edges = dict()
        in_edges = set()
        for p, q in zip(str1, str2):
            if p not in out_edges:
                out_edges[p] = q
                in_edges.add(q)
            elif out_edges[p] != q:
                return False
        return len(in_edges) < 26


# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/string-transforms-into-another-string/solution/python-dui-bi-str1zhong-shu-zhi-xiang-tong-de-wei-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        s = set(str2)
        if len(s) == 26:
            '''
            字符串2把所有字符种类26种都占满了，字符串1只有可能一开始也是占满26种字符才有转成功的可能性
            但是字符串1只要变换了第一次，总字符种类数一定变成25了，后面不管怎么变，字符种类数都是非递增
            的，不可能转换成功
            '''
            return False
        m = {}
        for i, ch in enumerate(str1):
            if ch not in m:
                m[ch] = str2[i]
            else:
                if m[ch] != str2[i]:
                    return False
        return True




S = Solution()
str1 = "aabcc"
str2 = "ccdee"
print(S.canConvert(str1, str2))
str1 = "leetcode"
str2 = "codeleet"
print(S.canConvert(str1, str2))
str1 ="ab"
str2 ="ba"
"""
ab => xa => ba
"""
print(S.canConvert(str1, str2))

str1 ="abcdefghijklmnopqrstuvwxyz"
str2 ="bcdefghijklmnopqrstuvwxyza"
print(S.canConvert(str1, str2))

str1 ="abcdefghijklmnopqrstuvwxyz"
str2 ="bcdefghijklmnopqrstuvwxyzq"
print(S.canConvert(str1, str2))
# 输出：
# false
# 预期结果：
# true