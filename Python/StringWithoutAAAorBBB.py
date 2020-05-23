"""
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"

Input: A = 7, B = 4
Output: "aabaabaabab"

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""
class Solution_1:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ''
        a, b = 'a', 'b'
        if A < B:
            A, B = B, A
            a, b = 'b', 'a'
        flag_A = True
        while A > 0 or B > 0:
            # print(A,B)
            if flag_A:
                if A-B > 2:
                    res += a*2
                    A -= 2
                else:
                    res += (A-B)*a
                    A -= A-B
                flag_A = False
            else:
                res += b
                B -= 1
                flag_A = True
        return res

class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """

        def rec(A,B):
            if B == 0:
                return a*A
            if A == B:
                return (b+a)*A
            elif A - B >= 2:
                return a*2 + b + rec(A-2,B-1)
            else:
                return a + rec(A-1,B)

        a, b = 'a', 'b'
        if A < B:
            A, B = B, A
            a, b = 'b', 'a'
        return rec(A,B)


s = Solution()
print(s.strWithout3a3b(1,2))
print(s.strWithout3a3b(4,1))
print(s.strWithout3a3b(7,4))
print(s.strWithout3a3b(8,4))
print(s.strWithout3a3b(2,0))



