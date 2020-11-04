"""
Given a string S, return the number of substrings of length K with no repeated characters.

 

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.
 

Note:

1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-k-length-substrings-with-no-repeated-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        counts = Counter()
        length = len(S)
        res = 0
        k = 0
        for i in range(length):
            # print(S[i-K+1:i+1])
            if i-K >= 0:
                pre = S[i-K]
                counts[pre] -= 1
                if counts[pre] == 0:
                    del counts[pre]
                    k -= 1
                elif counts[pre] == 1:
                    k += 1
            curr = S[i]
            counts[curr] += 1
            if counts[curr] == 1:
                k += 1
            elif counts[curr] == 2:  #previous 1
                k -= 1
            res += (k == K)
            # print(S[i-K+1:i+1], counts, k, res)
        return res

from collections import Counter
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        counts = Counter(S[:K])
        length = len(S)
        k = sum(v == 1 for v in counts.values())
        res = int(k == K)
        for i in range(K, length):
            pre = S[i-K]
            curr = S[i]
            if pre != curr:
                counts[pre] -= 1
                counts[curr] += 1
                if counts[pre] == 0:
                    k -= 1
                elif counts[pre] == 1:
                    k += 1
                if counts[curr] == 2:
                    k -= 1
                elif counts[curr] == 1:
                    k += 1
            res += (k == K)
        return res



class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        memo = set()
        start = 0
        res = 0
        for end, v in enumerate(S):
            while v in memo:
                memo.remove(S[start])
                start += 1
            memo.add(v)
            if end - start + 1 == K:
                res += 1
                memo.remove(S[start])
                start += 1
        return res

Slt = Solution()
S = "havefunonleetcode"
K = 5
print(Slt.numKLenSubstrNoRepeats(S, K))
S = "home"
K = 5
print(Slt.numKLenSubstrNoRepeats(S, K))
S = "gdggdbjchgadcfddfahbdebjbagaicgeahehjhdfghadbcbbfhgefcihbcbjjibjdhfhbdijehhiabad"
K = 5
print(Slt.numKLenSubstrNoRepeats(S, K))