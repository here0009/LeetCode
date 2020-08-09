"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"
 

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.
"""


from collections import deque
class Solution:
    def makeGood(self, string: str) -> str:
        res = list(string)
        gap = ord('a') - ord('A')
        # print(gap)
        while len(res) > 1:
            for i in range(1, len(res)):
                if abs(ord(res[i-1]) - ord(res[i])) == gap:
                    res2 = res[:i-1] + res[i+1:]
                    res = res2
                    break
            else:
                return ''.join(res)
        return ''.join(res)


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s: 
            if stack and abs(ord(stack[-1]) - ord(c)) == 32: 
                stack.pop() #pop "bad"
            else: 
                stack.append(c) #push "good"
        return "".join(stack)
S = Solution()
string = "leEeetcode"
print(S.makeGood(string))
string = "abBAcC"
print(S.makeGood(string))
string = "s"
print(S.makeGood(string))