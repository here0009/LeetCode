"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
"""
Thoughts: 
A needs to repeat math.ceil(len(B)/len(A)) times to cover B at least
A needs to repeat math.ceil(len(B)/len(A))+1 times to cover B at most, add another extra A do not add any subsequences at the length of B.
"""
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        k = len(B) // len(A)
        for i in range(3):
            if B in A*(k+i):
                return k+i
        return -1 

s = Solution()
A = "abcd"
B = "cdabcdab"
print(s.repeatedStringMatch(A,B))

