"""
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-way-to-form-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s_index = defaultdict(list)
        for i,v in enumerate(source):
            s_index[v].append(i)
        res = 0
        index = float('inf')
        for v in target:
            if v not in s_index:
                return -1
            lst = s_index[v]
            for i in lst:
                if i > index:
                    index = i
                    break
            else:
                index = lst[0]
                res += 1
        return res

S = Solution()
source = "abc"
target = "abcbc"
print(S.shortestWay(source, target))
source = "abc"
target = "acdbc"
print(S.shortestWay(source, target))
source = "xyz"
target = "xzyxz"
print(S.shortestWay(source, target))