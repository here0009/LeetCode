"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        """
        TLE for test cases got multiple origins
        """
        def dfs(si, ti):
            if ti == len_t:
                return si
            v = T[ti]
            # print(si, ti, v, s_index[v])
            if v not in s_index or s_index[v][-1] <= si:
                return float('inf')
            for j in s_index[v]:
                if j > si:
                    return dfs(j, ti+1)

        len_t = len(T)
        s_index = defaultdict(list)
        for i,v in enumerate(S):
            s_index[v].append(i)
        if len_t == 1:
            if T in s_index:
                return T
            else:
                return ''
        # print(s_index)
        res_len, res = float('inf'), (len(S), 2*len(S))
        for start in s_index[T[0]]:
            end = dfs(start, 1)
            d = end - start + 1
            # print(start, end, S[start:end+1], d)
            if d < res_len or (d == res_len and start < res[0]):
                res_len = d
                res = (start, end)

        return '' if res_len == float('inf') else S[res[0]:res[1]+1]


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        len_s, len_t = len(S), len(T)
        dp = [[(0, len_s)]*(len_t + 1) for _ in range(len_s + 1)]  # record the alignment score and start
        res_len, res = float('inf'), (len(S), 2*len(S))
        for i in range(1, len_s+1):
            for j in range(1, len_t+1):
                if j == 1 and S[i-1] == T[j-1]:
                    dp[i][j] = (1, i-1)
                else:
                    a, b = dp[i-1][j-1]
                    dp[i][j] = max((a+(S[i-1]==T[j-1]), b), dp[i-1][j], dp[i][j-1])
                score, start = dp[i][j]
                if score == len_t:
                    d = i - start + 1
                    if d < res_len:
                        res_len = d
                        res = (start, i-1)
                    elif d == res_len and start < res[0]:
                        res = (start, i-1)

        return '' if res_len == float('inf') else S[res[0]:res[1]+1]


# 作者：gao-xian-feng
# 链接：https://leetcode-cn.com/problems/minimum-window-subsequence/solution/zheng-fan-pi-pei-yi-wen-zhong-zhong-zui-zhong-xiu-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        lenS = len(S)
        lenT = len(T)
        s0 = 0
        e0 = lenS+1

        def findleagal(start):
            # 找到从start开始的符合条件的S的最短子串，返回的为区间结束点j
            k = 0
            for i in range(start, lenS):
                if S[i] == T[k]:
                    k += 1
                if k == lenT:
                    return i
            return -1

        def findshortest(j):
            # 从j逆向搜索找到k
            assert S[j] == T[-1]
            k = lenT - 1
            for i in range(j, -1, -1):
                if S[i] == T[k]:
                    k -= 1
                if k == -1:
                    return i
        i = 0
        while i < lenS:
            j = findleagal(i)
            if j == -1:
                break
            i = findshortest(j)
            if j - i + 1 < e0 - s0:
                s0 = i
                e0 = j + 1
            i += 1

        return S[s0:e0] if e0 - s0 != lenS+1 else ""

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/minimum-window-subsequence/solution/zui-xiao-chuang-kou-zi-xu-lie-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def minWindow(self, S, T):
        cur = [i if x == T[0] else None
               for i, x in enumerate(S)]
        #At time j when considering T[:j+1],
        #the smallest window [s, e] where S[e] == T[j]
        #is represented by cur[e] = s.
        for j in xrange(1, len(T)):
            last = None
            new = [None] * len(S)
            #Now we would like to calculate the candidate windows
            #"new" for T[:j+1].  'last' is the last window seen.
            for i, u in enumerate(S):
                if last is not None and u == T[j]: new[i] = last
                if cur[i] is not None: last = cur[i]
            cur = new

        #Looking at the window data cur, choose the smallest length
        #window [s, e].
        ans = 0, len(S)
        for e, s in enumerate(cur):
            if s >= 0 and e - s < ans[1] - ans[0]:
                ans = s, e
        return S[ans[0]: ans[1]+1] if ans[1] < len(S) else ""


# 作者：Matrix95
# 链接：https://leetcode-cn.com/problems/minimum-window-subsequence/solution/dong-tai-gui-hua-by-matrix95/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = len(T)
        n = len(S)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for j in range(n+1):
            dp[0][j] = j + 1
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if T[i-1] == S[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        start = 0
        l = n+1
        for j in range(1,n+1):
            if dp[m][j] :
                if j - dp[m][j] + 1 < l:
                    start = dp[m][j]-1
                    l = j - dp[m][j] + 1
        return "" if l == n+1 else S[start:start+l]


s = Solution()
S = "abcdebdde"
T = "bde"
print(s.minWindow(S, T))

S = "cnhczmccqouqadqtmjjzl"
T ="cm"
print(s.minWindow(S, T))
# 输出：
# "cnhczm"
# 预期结果：
# "czm"

S = "bde"
T = "bde"
print(s.minWindow(S, T))
