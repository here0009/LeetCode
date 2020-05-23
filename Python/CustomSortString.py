"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        S_dict = {}
        int_dict ={}
        for i,s in enumerate(S):
            S_dict[s] = i
            int_dict[i] = s
        T_list = [k for k in T]
        # print(T_list)
        sort_T = []
        remain_T = []
        for t in T_list:
            if t in S_dict:
                sort_T.append(S_dict[t])
            else:
                remain_T.append(t)

        sort_T = sorted(sort_T)
        for i,t in enumerate(sort_T):
            sort_T[i] = int_dict[t]
        # print(sort_T)
        # print(remain_T)
        return ''.join(sort_T) + ''.join(remain_T)

from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        T_counter = Counter(T)
        res = ''
        for s in S:
            if s in T_counter:
                res += s * T_counter[s]
        for t in T:
            if t not in S:
                res += t
        return res

s = Solution()
S = "cba"
T = "abcd"
print(s.customSortString(S,T))

