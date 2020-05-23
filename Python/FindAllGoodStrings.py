"""
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 
Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.
"""
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        if s2 < s1:
            return 0
        prefix = ''
        index = 0
        len_e = len(evil)
        while index < n and s1[index] == s2[index]:
            prefix += s1[index]
            index += 1
        if evil in prefix:
            return 0
        res = 1 #for s1 itself
        while index < n:
            res += 26**(n-index-1)*(ord(s2[index])-ord(s1[index]))
            index += 1

        s_index, evil_index = 0,0
        for index in range(n-len_e):
            if evil >= s1[index:index+len_e] and evil <= s2[index:index+len_e]:
                res -= 26**(n-index-1-1)
        return res

S = Solution()
n = 2
s1 = "aa"
s2 = "da"
evil = "b"
print(S.findGoodStrings(n,s1,s2,evil))
n = 8
s1 = "leetcode"
s2 = "leetgoes"
evil = "leet"
print(S.findGoodStrings(n,s1,s2,evil))
n = 2
s1 = "gx"
s2 = "gz"
evil = "x"
print(S.findGoodStrings(n,s1,s2,evil))