"""
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".
 

Constraints:

1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.
"""
"""
substring, not any order of letters
"""
class Solution_1:
    def balancedString(self, string: str) -> int:
        k = len(string)//4
        letters = "QWER"
        counts = {l:0 for l in letters}
        for l in string:
            counts[l] += 1
        print(k,counts)
        return sum([abs(k-v) for v in counts.values()])//2
        # res = 0
        # for letter, value in counts.items():
        #     res += abs(k-value)
        # return res//2
from collections import deque
class Solution:
    def balancedString(self, string: str) -> int:
        #find the min len of substring contain extra letters
        b = len(string)//4
        letters = "QWER"
        counts = {l:0 for l in letters}
        for l in string:
            counts[l] += 1
        res = len(string)
        target = {l:0 for l in letters}
        tmp = {l:0 for l in letters}
        for k,v in counts.items():
            if v > b:
                target[k] += v-b
        # print(target)
        q = deque()
        for l in string:
            q.append(l)
            tmp[l] += 1
            for k in target.keys():
                if tmp[k] < target[k]:
                    break
            else:
                while q and tmp[q[0]] > target[q[0]]:
                    tmp[q.popleft()] -= 1
                res = min(res, len(q))
        return res

s = Solution()
string = "QWER"
print(s.balancedString(string))

string = "QQWE"
print(s.balancedString(string))


string = "QQQW"
print(s.balancedString(string))

string = "QQQQ"
print(s.balancedString(string))

string = "WWEQERQWQWWRWWERQWEQ"
print(s.balancedString(string))

# Output:
# 3
# Expected:
# 4
