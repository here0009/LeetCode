"""
Given strings A and B of the same length, we say A[i] and B[i] are equivalent characters. For example, if A = "abc" and B = "cde", then we have 'a' == 'c', 'b' == 'd', 'c' == 'e'.

Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'
Symmetry: 'a' == 'b' implies 'b' == 'a'
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'
For example, given the equivalency information from A and B above, S = "eed", "acd", and "aab" are equivalent strings, and "aab" is the lexicographically smallest equivalent string of S.

Return the lexicographically smallest equivalent string of S by using the equivalency information from A and B.

 

Example 1:

Input: A = "parker", B = "morris", S = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in A and B, we can group their characters as [m,p], [a,o], [k,r,s], [e,i]. The characters in each group are equivalent and sorted in lexicographical order. So the answer is "makkek".
Example 2:

Input: A = "hello", B = "world", S = "hold"
Output: "hdld"
Explanation:  Based on the equivalency information in A and B, we can group their characters as [h,w], [d,e,o], [l,r]. So only the second letter 'o' in S is changed to 'd', the answer is "hdld".
Example 3:

Input: A = "leetcode", B = "programs", S = "sourcecode"
Output: "aauaaaaada"
Explanation:  We group the equivalent characters in A and B as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in S except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
 

Note:

String A, B and S consist of only lowercase English letters from 'a' - 'z'.
The lengths of string A, B and S are between 1 and 1000.
String A and B are of the same length.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lexicographically-smallest-equivalent-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        def find(i):
            if i not in root:
                root[i] = i
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            if ri < rj:
                ri, rj = rj, ri
            root[ri] = rj
            return True

        root = dict()
        for p, q in zip(A, B):
            union(p, q)

        return ''.join(find(c) for c in S)

Slt = Solution()
A = "parker"
B = "morris"
S = "parser"
print(Slt.smallestEquivalentString(A, B, S))
A = "hello"
B = "world"
S = "hold"
print(Slt.smallestEquivalentString(A, B, S))
A = "leetcode"
B = "programs"
S = "sourcecode"
print(Slt.smallestEquivalentString(A, B, S))