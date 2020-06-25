"""
Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i+1 < j, such that:

A[0], A[1], ..., A[i] is the first part;
A[i+1], A[i+2], ..., A[j-1] is the second part, and
A[j], A[j+1], ..., A[A.length - 1] is the third part.
All three parts have equal binary value.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents.  For example, [1,1,0] represents 6 in decimal, not 3.  Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

 

Example 1:

Input: [1,0,1,0,1]
Output: [0,3]
Example 2:

Input: [1,1,0,1,1]
Output: [-1,-1]

Note:

3 <= A.length <= 30000
A[i] == 0 or A[i] == 1
"""


class Solution:
    def threeEqualParts(self, A):
        def lsttobin(lst):
            return int(''.join([str(i) for i in lst]), 2)

        # print(A)
        impossible = [-1,-1]
        length = len(A)
        total = sum(A)
        if total == 0:
            return [0, length-1]
        if total % 3 != 0:
            return impossible
        target = total // 3
        count = 0
        index_list = []
        # print(target)
        for i,v in enumerate(A):
            if v:
                count += 1
                if count == 1:
                    index_list.append(i)
                if count == target:
                    count = 0
        # print(index_list)
        if len(index_list) != 3:
            return impossible
        sublength = length - index_list[-1]
        
        i,k,j = index_list
        i2,k2,j2 = lsttobin(A[i:i+sublength]), lsttobin(A[k:k+sublength]), lsttobin(A[j:j+sublength])
        # print(i,k,j)
        # print(i2,k2,j2)
        if i2 == k2 and k2 == j2:
            return [i+sublength-1, k+sublength]
        else:
            return impossible

S = Solution()
A = [1,0,1,0,1]
print(S.threeEqualParts(A))
A = [1,1,0,1,1]
print(S.threeEqualParts(A))

A = [0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,0]
print(S.threeEqualParts(A))
A = [0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1]
print(S.threeEqualParts(A))
A = [1,1,1,1,1,1,0,1,1,1]
print(S.threeEqualParts(A))
A = [0,1,0,1,1,0,1,1,0,1]
print(S.threeEqualParts(A))