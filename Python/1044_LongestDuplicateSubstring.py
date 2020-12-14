"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        TLE 62/63
        """
        def calc(s1, s2):
            length = min(len(s1), len(s2))
            i = 0
            while i < length and s1[i] == s2[i]:
                i += 1
            return i, s1[:i]

        suffix_arry = []
        len_s = len(s) -1
        for i in range(len_s):
            suffix_arry.append(s[i:])
        suffix_arry.sort()
        max_len, res = 0, ''
        for i in range(1, len(suffix_arry)):
            tmp_len, tmp_str = calc(suffix_arry[i], suffix_arry[i-1])
            if tmp_len > max_len:
                max_len = tmp_len
                res = tmp_str
        return res

"""
1. find the max length of a single repeated letter, so the length of res is a lest len(max(single_repeated_lette)) - 1, we record the length as max_len, the string as res
2. construct suffix_arry, the min length of the suffix is previous found max_len + 1
3. sort the suffix_arry and calculate the score between ajacent suffix, update max_len and res
"""
class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def calc(s1, s2):
            length = min(len(s1), len(s2))
            i = 0
            while i < length and s1[i] == s2[i]:
                i += 1
            return i, s1[:i]

        # find the max continous repeat single letter, max_len is len(max(single_repeated_lette)) - 1
        len_s = len(s)
        i, pre = -1, None
        max_len, res = 0, ''
        for j, v in enumerate(s):
            if v != pre or j == len_s-1:
                tmp_len = j-i # tmp_len is the length of repeat character
                if tmp_len-1 > max_len:
                    max_len = tmp_len-1
                    res = pre*max_len
                i = j
                pre = v

        suffix_arry = []
        for i in range(len_s - max_len): # len_s - max_len will be ok, will only need to calculate arrays that got length larger than max_len +1, so the last index is lens-maxlen-1
            suffix_arry.append(s[i:])
        suffix_arry.sort()

        for i in range(1, len(suffix_arry)):
            tmp_len, tmp_str = calc(suffix_arry[i], suffix_arry[i-1])
            if tmp_len > max_len:
                max_len = tmp_len
                res = tmp_str
        return res


from functools import reduce
from collections import defaultdict
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def test(len_k):
            p = 26**len_k % M
            pos_dict = defaultdict(list)
            curr = reduce(lambda x, y: (x * 26 + y) % M, num_s[:len_k])
            pos_dict[curr].append(0)
            for i in range(1, len_s - len_k + 1):
                curr = (curr * 26 - num_s[i - 1] * p + num_s[i - 1 + len_k]) % M
                for j in pos_dict[curr]:
                    if s[i:i + len_k] == s[j:j + len_k]:
                        return s[i:i + len_k]
                pos_dict[curr].append(i)
            return ''

        num_s = [ord(i) - ord('a') for i in s]
        len_s = len(num_s)
        M = 10**9 + 7
        left, right = 1, len(s) - 1
        res = ''
        while left <= right:
            mid = (left + right) // 2
            tmp = test(mid)
            # print(left, right, mid, tmp)
            if tmp != '':
                left = mid + 1
                res = tmp
            else:
                right = mid - 1
        return res

S = Solution()
print(S.longestDupSubstring("banana"))
print(S.longestDupSubstring("abcd"))