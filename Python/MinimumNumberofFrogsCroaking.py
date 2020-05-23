"""
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1
 

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
"""
from collections import Counter
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        rmd = Counter()
        pre_dict = dict()
        croak = 'croakc'
        for i in range(1,len(croak)):
            pre_dict[croak[i]] = croak[i-1]
        print(pre_dict)
        stack = []
        for letter in croakOfFrogs:
            stack.append(letter)
            while stack and rmd[pre_dict[stack[-1]]] > 0:
                tmp = stack.pop()
                next_tmp = pre_dict[tmp]
                rmd[tmp] -= 1
                rmd[next_tmp] += 1
                rmd[stack[-1]] += 1
        print(rmd)
        return rmd['c']

from collections import Counter
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = list("croak")
        counter = {c:1 for c in croak}
        res = 0
        for c in croakOfFrogs:
            if c not in counter:
                return -1
            counter[c] += 1
            res = max(res,counter['c']-counter['k'])
            for i in range(1,5):
                if counter[croak[i]] > counter[croak[i-1]]:
                    return -1
        for i in range(1,5):
            if counter[croak[i]] != counter[croak[i-1]]:
                return -1
        return res

S = Solution()
croakOfFrogs = "croakcroak"
print(S.minNumberOfFrogs(croakOfFrogs))
croakOfFrogs = "crcoakroak"
print(S.minNumberOfFrogs(croakOfFrogs))
croakOfFrogs = "croakcrook"
print(S.minNumberOfFrogs(croakOfFrogs))
croakOfFrogs = "croakcroa"
print(S.minNumberOfFrogs(croakOfFrogs))