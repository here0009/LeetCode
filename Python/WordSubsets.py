"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
 

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
from collections import Counter
class Solution:
    def wordSubsets(self, A, B):
        def isSubset(counter_a, counter_b):
            for b,v in counter_b.items():
                if b not in counter_a or counter_b[b] > counter_a[b]:
                    return False
            return True

        A_counter = [Counter(w) for w in A]
        b_merge = Counter()
        for b in B:
            b_merge = b_merge | Counter(b)
            # for key,v in counter.items():
            #     b_merge[key] = max(b_merge[key],v)
        # print(b_merge)
        res = []
        for i,a in enumerate(A_counter):
            if isSubset(a, b_merge):
                res.append(A[i])
        return res

from collections import Counter
class Solution:
    def wordSubsets(self, A, B):
        b_merge = Counter()
        for b in B:
            b_merge = b_merge | Counter(b)
        res = [a for a in A if b_merge & Counter(a) == b_merge]
        return res


s = Solution()
A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]
print(s.wordSubsets(A,B))

B = ["l","e"]
print(s.wordSubsets(A,B))

B = ["e","oo"]
print(s.wordSubsets(A,B))

B = ["lo","eo"]
print(s.wordSubsets(A,B))

B = ["ec","oc","ceo"]
print(s.wordSubsets(A,B))