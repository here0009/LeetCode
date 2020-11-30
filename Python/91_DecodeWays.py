"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution_1:
    def numDecodings(self, string: str) -> int:
        """
        wrong
        """
        string = string.lstrip('0')
        print(string)
        if len(string) < 2:
            return len(string)
        if len(string) == 2:
            if int(string) < 27:
                return 2
            else:
                return 1
        res = 1
        for i in range(1,len(string)):
            res += self.numDecodings(string[:i])*self.numDecodings(string[i:])-1
        return res

class Solution:
    def numDecodings(self, string: str) -> int:
        int_string = int(string[0])
        if int_string == 0:
            return 0
        odd, even = 1,1
        for i in range(0, len(string),2):
            letter = string[i:i+2]#.strip('0')
            num = int(letter)
            if num > 0 and num <= 10:
                if num != 10 and len(letter) == 2:
                    even = 0
                    break
            elif num > 10 and num < 27:
                even *= 2
            else:
                even = 0
                break

        for i in range(1, len(string),2):
            letter = string[i:i+2]#.strip('0')
            num = int(letter)
            if num > 0 and num <= 10:
                if num != 10 and len(letter) == 2:
                    odd = 0
                    break
            elif num > 10 and num < 27:
                odd *= 2
            else:
                odd = 0
                break
        if even > 0 and odd > 0:
            return even+odd-1
        else:
            return even+odd


class Solution:
    def numDecodings(self, string: str) -> int:
        pre = ''
        res = 0
        for s in string:
            if not pre:
                pre = s
            else:
                n2 = int(pre+s)
                if n2 >= 10 and n2 <=26:
                    res += 1
                if s == '0':
                    if pre != '1' and pre != '2':
                        return 0
                    else:
                        pre = ''
                else:
                    # res += 1
                    pre = s
            if pre == '0':
                return 0
            else:
                res += 1
        return res

from functools import lru_cache
class Solution:
    def numDecodings(self, string: str) -> int:
        @lru_cache(None)
        def dp(string):
            if string[0] == '0':
                return 0
            if len(string) == 1:
                return 1
            res = dp(string[:1])*dp(string[1:])
            if 10 <= int(string[:2]) <= 26:
                res += dp(string[2:]) if len(string) > 2 else 1
            return res

        if not string or string[0] == '0':
            return 0
        return dp(string)

class Solution:
    def numDecodings(self, string: str) -> int:
        if not string or string[0] == '0':
            return 0
        length = len(string)
        dp = [0]*(length+1) #dp[i] stand for the ways to decode string[:i]
        dp[0], dp[1] = 1, 1
        for i in range(2, length+1):
            if string[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(string[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


s = Solution()
string = '12'
print(s.numDecodings(string))

string = '226'
print(s.numDecodings(string))

# string = '1221'
# print(s.numDecodings(string))

# string = "0"
# print(s.numDecodings(string))

# string = "101"
# print(s.numDecodings(string))

# string = "110"
# print(s.numDecodings(string))

# string = "01"
# print(s.numDecodings(string))

# string = "100"
# print(s.numDecodings(string))

# string = "230"
# print(s.numDecodings(string))

# string = "301"
# print(s.numDecodings(string))

string = "2611055971756562"
print(s.numDecodings(string))
# Output
# 2
# Expected
# 4