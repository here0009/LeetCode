"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""
from collections import Counter
class Solution:
    def commonChars(self, A):
        c_set = set(A[0])
        counter_list = []
        res = []
        for s in A:
            counter_list.append(Counter(s))
            c_set = c_set & set(s)

        for c in c_set:
            copies = min([counter[c] for counter in counter_list])
            res.extend([c]*copies)
        return res

s = Solution()
A = ["bella","label","roller"]
print(s.commonChars(A))

A = ["cool","lock","cook"]
print(s.commonChars(A))

A = ["cool"]
print(s.commonChars(A))

A = ["k"]
print(s.commonChars(A))

