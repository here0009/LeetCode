"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
"""
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for s in S:
            if s.isdigit():
                res = [string+str(s) for string in res]
            else:
                s = s.lower()
                tmp = [string+s for string in res]
                s = s.upper()
                res = [string+s for string in res]
                res.extend(tmp)
        return res

test = "a1b2"
s = Solution()
print(s.letterCasePermutation(test))
test = "3z4"
print(s.letterCasePermutation(test))
test = "12345"
print(s.letterCasePermutation(test))