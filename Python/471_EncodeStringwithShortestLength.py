"""
Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
 

Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
 

Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
 

Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 

Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
 

Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/encode-string-with-shortest-length
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 作者：ljbupt
# 链接：https://leetcode-cn.com/problems/encode-string-with-shortest-length/solution/python-solution-with-comments-by-ljbupt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def encode(self, s: str) -> str:
        # Dynamic programming 
        # dp[i][j]: encoding for string s[i : j + 1] with shortest length

        if not s:
            return s

        # create 2d dp with size len(s) * len(s)
        dp = [[s] * len(s) for i in range(len(s))]
        
        for width in range(1, len(s) + 1):
            # first round: generate dp[0][0], dp[1][1], dp[2][2], ..., dp[n - 1][n - 1]
            # second round: generate dp[0][1], dp[1][2], dp[2][3], ...., dp[n - 2][n - 1]
            # ......
            # last round: generate dp[0][n - 1], which is the return value

            for i in range(0, len(s) - width + 1):
                j = i + width - 1
                if width < 5:
                    dp[i][j] = s[i: j + 1]
                    continue 

                substr = s[i: j + 1]
                repIdx = (substr + substr).find(substr, 1)  # start from 1 to skip s itself

                # case1: substr is repeat of some str
                if repIdx < width:
                    dp[i][j] = (str)((int) (width / repIdx)) + '[' + dp[i][repIdx + i - 1] + ']' # be careful, here use dp[i][repIdx - 1] instead of substr[:repIdx]

                # case2: substr is not a self repeat str, update dp[i][j] with dp[i][k] + dp[k + 1][j]
                else:
                    for k in range(i, j):
                        dp[i][j] = dp[i][k] + dp[k + 1][j] if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]) else dp[i][j]
        return dp[0][-1]

# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/encode-string-with-shortest-length/solution/python-di-gui-ya-suo-zi-fu-chuan-shuang-100-by-hao/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# from functools import lru_cache

'''
递归进行压缩，把s切分成两半，左边一半如果能够按照整倍数压缩，就进行压缩，先把左边一半变成最短的，
然后递归处理右边一半，把两半都处理完之后的字符串拼接回来，最短的拼接字符串就是答案，判断能不能进行
整倍数压缩的时候，问题转换为找串的重复子串问题
'''

from functools import lru_cache
class Solution:

    #  返回最短的以倍数压缩后的字符串，不能压缩返回原字符串
    @lru_cache(None)
    def compress(self, s: str):
        if s == '' or len(s) == 1:
            return s

        t = s + s
        n = len(s)
        ans = s

        # 找重复子串位置
        idx = t.find(s, 1)
        if idx == n:
            return ans

        cnt = len(s) // idx
        encode_str = self.encode(s[:idx])
        ss = str(cnt) + '[' + encode_str + ']'
        if len(ss) < len(ans):
            ans = ss
        return ans

    @lru_cache(None)
    def encode(self, s: str) -> str:
        #print(s)
        if s == '' or len(s) == 1:
            return s

        ans = s
        for i in range(0, len(s)):
            ss = self.compress(s[:i+1]) + self.encode(s[i+1:])
            if len(ss) < len(ans):
                ans = ss
        return ans


from functools import lru_cache
class Solution:
    @lru_cache(None)
    def compress(self, s):
        length = len(s)
        if length <= 1:
            return s
        t = s + s
        index = t.find(s, 1)
        if index == length:  # can not be compressed
            return s
        elem = self.encode(s[:index])  # element may be can still be encoded 
        counts = length//index
        encoded_s = '{}[{}]'.format(counts, elem)
        # print(s, encoded_s)
        return encoded_s if len(encoded_s) < length else s

    @lru_cache(None)
    def encode(self, s):
        length = len(s)
        if length <= 1:
            return s
        res = s
        for i in range(0, length):
            ss = self.compress(s[:i+1]) + self.encode(s[i+1:])
            if len(ss) < len(res):
                res = ss
        return res


S = Solution()
s = "aaa"
print(S.encode(s))
s = "aaaaa"
print(S.encode(s))
s = "aaaaaaaaaa"
print(S.encode(s))
s = "aabcaabcd"
print(S.encode(s))
s = "abbbabbbcabbbabbbc"
print(S.encode(s))