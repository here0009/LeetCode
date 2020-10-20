"""
You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

You can apply either of the following two operations any number of times and in any order on s:

Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.

 

Example 1:

Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the following operations:
Start:  "5525"
Rotate: "2555"
Add:    "2454"
Add:    "2353"
Rotate: "5323"
Add:    "5222"
​​​​​​​Add:    "5121"
​​​​​​​Rotate: "2151"
​​​​​​​Add:    "2050"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "2050".
Example 2:

Input: s = "74", a = 5, b = 1
Output: "24"
Explanation: We can apply the following operations:
Start:  "74"
Rotate: "47"
​​​​​​​Add:    "42"
​​​​​​​Rotate: "24"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "24".
Example 3:

Input: s = "0011", a = 4, b = 2
Output: "0011"
Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".
Example 4:

Input: s = "43987654", a = 7, b = 3
Output: "00553311"
 

Constraints:

2 <= s.length <= 100
s.length is even.
s consists of digits from 0 to 9 only.
1 <= a <= 9
1 <= b <= s.length - 1
"""


from functools import lru_cache
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        @lru_cache(None)
        def add(lst):
            lst = [int(num) for num in list(lst)]
            res = ['0']*length
            for i in range(length):
                if i % 2 == 1:
                    res[i] = str((lst[i]+a)%10)
                else:
                    res[i] = str(lst[i])
            return ''.join(res)

        @lru_cache(None)
        def shift(lst):
            lst = [int(num) for num in list(lst)]
            res = ['0']*length
            for i in range(length):
                res[i] = str(lst[(i-b)%length])
            return ''.join(res)

        def dfs(lst):
            # print(lst)
            if lst not in visited:
                visited.add(lst)
                dfs(add(lst))
                dfs(shift(lst))

        length = len(s)
        visited = set()
        # visited.add(s)
        dfs(s)
        # print(visited)
        return min(visited)


from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        dq = deque([s])
        visited = {s}
        res = s
        while dq:
            curr = dq.popleft()
            if curr < res:
                res = curr
            addA = list(curr)
            for i,c in enumerate(addA):
                if i % 2 == 1:
                    addA[i] = str((int(addA[i])+a)%10)
            addA = ''.join(addA)
            if addA not in visited:
                dq.append(addA)
                visited.add(addA)
            shiftB = curr[-b:] + curr[:-b]
            if shiftB not in visited:
                dq.append(shiftB)
                visited.add(shiftB)
        return res



S = Solution()
s = "5525"
a = 9
b = 2
print(S.findLexSmallestString(s, a, b))
s = "74"
a = 5
b = 1
print(S.findLexSmallestString(s, a, b))
s = "0011"
a = 4
b = 2
print(S.findLexSmallestString(s, a, b))
s = "43987654"
a = 7
b = 3
print(S.findLexSmallestString(s, a, b))