"""
Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.


Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".


Note:

S contains only lowercase letters.
1 <= S.length <= 2000
"""


from collections import Counter
class Solution:
    """
    dp, use subseqs to store the subsequences ends with a specific letter, total to store all the subsequences. so if a letter `k` is not seen before, it can join all the subsequences before and the newly formed subsequenes ends with `k` is total+1.
    if there are `k` before, the newly encountered `k` can not form subsequences with `k` before.
    it can form a subsequence like `kkk...`
    """
    def distinctSubseqII(self, string: str) -> int:
        M = 10**9 + 7
        subseqs = Counter()
        total = 0
        for letter in string:
            if letter not in counts:
                tmp = total + 1
            else:
                tmp = total - subseqs[letter] + 1
            subseqs[letter] += tmp
            total += tmp
            total = total % M
            counts[letter] += 1
        return total

        
from collections import Counter
class Solution:
    """
    dp, use subseqs to store the subsequences ends with a specific letter, total to store all the subsequences. so if a letter `k` is not seen before, it can join all the subsequences before and the newly formed subsequenes ends with `k` is total+1.
    if there are `k` before, the newly encountered `k` can not form subsequences end with `k` before.
    it can form a subsequence like `kkk...`, so +1
    """
    def distinctSubseqII(self, string: str) -> int:
        M = 10**9 + 7
        subseqs = Counter()
        total = 0
        for letter in string:
            tmp = total - subseqs[letter] + 1
            subseqs[letter] += tmp
            total += tmp
            total = total % M
        return total

S = Solution()
string = "abc"
print(S.distinctSubseqII(string))
string = "aba"
print(S.distinctSubseqII(string))
string = "aaa"
print(S.distinctSubseqII(string))