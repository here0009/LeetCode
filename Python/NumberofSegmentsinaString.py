"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""
import re
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(re.split('\s+',s.strip()))
        return sum([len(segment)>0 for segment in re.split('\s+',s.strip())])

S = Solution()
print(S.countSegments("Hello, my name is John"))
print(S.countSegments("Hello, my name is  John "))
print(S.countSegments(" "))