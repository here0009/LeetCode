"""
Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

0 <= s.length <= 3000
s consists of digits only.
"""


class Solution:
    def restoreIpAddresses(self, string: str):
        def valid(string):
            return str(int(string)) == string and (0 <= int(string) < 256)

        def dfs(string, n, path):
            if not string:
                return
            if n == 1:
                if valid(string):
                    path += string
                    self.res.append(path)
            else:
                for i in range(1, 4):
                    pre = string[:i]
                    if valid(pre):
                        dfs(string[i:], n-1, path+pre+'.')
        self.res = []
        dfs(string, 4, '')
        return self.res

S = Solution()
string = "25525511135"
print(S.restoreIpAddresses(string))
string = "0000"
print(S.restoreIpAddresses(string))
string = "1111"
print(S.restoreIpAddresses(string))
string = "010010"
print(S.restoreIpAddresses(string))
string = "101023"
print(S.restoreIpAddresses(string))
