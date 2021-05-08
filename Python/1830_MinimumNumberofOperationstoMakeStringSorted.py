"""
You are given a string s (0-indexed)​​​​​​. You are asked to perform the following operation on s​​​​​​ until you get a sorted string:

Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
Swap the two characters at indices i - 1​​​​ and j​​​​​.
Reverse the suffix starting at index i​​​​​​.
Return the number of operations needed to make the string sorted. Since the answer can be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "cba"
Output: 5
Explanation: The simulation goes as follows:
Operation 1: i=2, j=2. Swap s[1] and s[2] to get s="cab", then reverse the suffix starting at 2. Now, s="cab".
Operation 2: i=1, j=2. Swap s[0] and s[2] to get s="bac", then reverse the suffix starting at 1. Now, s="bca".
Operation 3: i=2, j=2. Swap s[1] and s[2] to get s="bac", then reverse the suffix starting at 2. Now, s="bac".
Operation 4: i=1, j=1. Swap s[0] and s[1] to get s="abc", then reverse the suffix starting at 1. Now, s="acb".
Operation 5: i=2, j=2. Swap s[1] and s[2] to get s="abc", then reverse the suffix starting at 2. Now, s="abc".
Example 2:

Input: s = "aabaa"
Output: 2
Explanation: The simulation goes as follows:
Operation 1: i=3, j=4. Swap s[2] and s[4] to get s="aaaab", then reverse the substring starting at 3. Now, s="aaaba".
Operation 2: i=4, j=4. Swap s[3] and s[4] to get s="aaaab", then reverse the substring starting at 4. Now, s="aaaab".
Example 3:

Input: s = "cdbea"
Output: 63
Example 4:

Input: s = "leetcodeleetcodeleetcode"
Output: 982157772
 

Constraints:

1 <= s.length <= 3000
s​​​​​​ consists only of lowercase English letters.
"""


from functools import lru_cache
class Solution:
    def makeStringSorted(self, string: str) -> int:
        """
        TLE
        """

        @lru_cache(None)
        def calc(string):
            print(string)
            i = len(string) - 1
            while i > 0 and string[i - 1] <= string[i]:
                i -= 1
            if i == 0:
                return 0
            j = len(string) - 1
            while j > i and string[i - 1] <= string[j]:
                j -= 1
            lst = list(string)
            lst[i - 1], lst[j] = lst[j], lst[i - 1]
            return ''.join(lst[:i] + lst[i:][::-1])

        res = 0
        M = 10**9 + 7
        while (s2 := calc(string)) != 0:
            string = s2
            res += 1
        return res


class Solution:
    def makeStringSorted(self, s: str) -> int:
        # 求字符串的总共组合数量，用到了那个先验知识
        cnt = collections.Counter(s)
        cur = math.factorial(len(s))
        for v in cnt.values():
            cur //= math.factorial(v)

        res = 0
        for i, v in enumerate(s):
            for ke, va in cnt.items():
                # 当后续某个字符小于当前字符，累加当前的可能性
                # 以上面的描述为例，当b后面出现个a，可以假定当前位置变成a，这种情况下
                # 还剩下 (x - 1)个a，y个b，z个c, 组合总数为 ((x - 1) + y + z)! / ((x - 1)! * y! * z!)
                # 等同为 (x + y + z)! / (x! * y! * z!) * x / (x + y + z)
                # 也就是下面的 cur * va // (len(s) - i)
                if ke < v:
                    res += cur * va // (len(s) - i)

            # 当字符往后移动时，更新当前的可能的组合数，同时更新Counter
            cur = cur * cnt[v] // (len(s) - i)
            cnt[v] -= 1

        return res % (10 ** 9 + 7)

# 作者：semirondo
# 链接：https://leetcode-cn.com/problems/minimum-number-of-operations-to-make-string-sorted/solution/bi-jiao-hao-li-jie-de-pythondai-ma-by-se-f4tw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from functools import lru_cache
class Solution:
    def makeStringSorted(self, string: str) -> int:
        """
        Reverse the process, how many steps do we need to get string from a sorted string.
        string is the lexi order of the permuation
        """

S = Solution()
# string = "cba"
# print(S.makeStringSorted(string))
# string = "aabaa"
# print(S.makeStringSorted(string))
string = "cdbea"
print(S.makeStringSorted(string))
# string = "leetcodeleetcodeleetcode"
# print(S.makeStringSorted(string))
# string = "leetcodeleetcode"
# print(S.makeStringSorted(string))