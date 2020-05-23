"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
"""
class Solution_1:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        unequals = []
        max_counts = 0
        counts_dict = dict()
        for i in range(len(A)):
            if A[i] != B[i]:
                unequals.append(i)
            else:
                counts_dict[A[i]] = counts_dict.get(A[i],0) + 1
                max_counts = max(max_counts, counts_dict[A[i]])
        # print(unequals)
        if len(unequals) == 0 and max_counts > 1:
            return True
        if len(unequals) == 2 and A[unequals[0]] == B[unequals[1]] and B[unequals[0]] == A[unequals[1]]:
            return True
        return False

class Solution:
    """
    Thoughts: Use set to replace dict, more faster
    """
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        unequals = []
        
        for i in range(len(A)):
            if A[i] != B[i]:
                unequals.append(i)

        # print(unequals)
        if len(unequals) == 0 and len(set(A)) < len(A): #repeat letters, can swap the repeated ones
            return True
        if len(unequals) == 2 and A[unequals[0]] == B[unequals[1]] and B[unequals[0]] == A[unequals[1]]:
            return True
        return False

s = Solution()
A = "ab"
B = "ba"
print(s.buddyStrings(A,B))

A = "ab"
B = "ab"
print(s.buddyStrings(A,B))

A = "aa"
B = "aa"
print(s.buddyStrings(A,B))

A = "aaaaaaabc"
B = "aaaaaaacb"
print(s.buddyStrings(A,B))

A = ""
B = "aa"
print(s.buddyStrings(A,B))

A = "ab"
B = "ca"
print(s.buddyStrings(A,B))