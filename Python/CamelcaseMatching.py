"""
A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

 

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: 
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: 
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Note:

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.
"""
import re
class Solution:
    def camelMatch(self, queries, pattern: str):
        res = []
        re_pattern = r'^[a-z]*'
        re_pattern += pattern[0]
        for letter in pattern[1:]:
            # if letter.isupper():
            re_pattern += r'[a-z]*'
            re_pattern += letter
        re_pattern += r'[a-z]*$'
        # print(re_pattern)
        for query in queries:
            if re.search(re_pattern, query):
                res.append(True)
            else:
                res.append(False)
        return res

s = Solution()
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
print(s.camelMatch(queries,pattern))

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBa"
print(s.camelMatch(queries,pattern))

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"
print(s.camelMatch(queries,pattern))

queries = ["CompetitiveProgramming","CounterPick","ControlPanel"]
pattern = "CooP"
print(s.camelMatch(queries,pattern))

queries = ["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"]
pattern = "ksvjLiknTzqn"
print(s.camelMatch(queries,pattern))