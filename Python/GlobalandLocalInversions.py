"""
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
"""
class Solution:
    def isIdealPermutation(self, A) -> bool:
        g_inv, l_inv = 0, 0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                l_inv += 1
        sorted_A = sorted([(v,i) for i,v in enumerate(A)])
        # print(sorted_A)
        larger_nums = set()
        for i,v in enumerate(A):
            if i in larger_nums:
                larger_nums.remove(i)
            if v > i:
                larger_nums.add(v)
                g_inv += v-i #the inversions that will created by v
            elif v == i:
                g_inv += len(larger_nums) #v == i, so v is at the right place, counts the nums that larger than i appears befor
        return g_inv == l_inv


class Solution:
    def isIdealPermutation(self, A) -> bool:
        """
        Thoughts: local_inversion == global_inversion means all global inversions are local inversion. So if we find a global inversion but it is not a local inversion, return False
        """
        max_num = 0
        for i in range(len(A)-2):
            max_num = max(max_num, A[i])
            if max_num > A[i+2]: #max_num > A[i+1] 
                return False
        return True

class Solution:
    def isIdealPermutation(self, A) -> bool:
        return all(abs(i-v) <= 1 for i,v in enumerate(A)) #if i-v<=1 it is a local inversion, otherwise it is a global inversion

S = Solution()
A = [1,0,2]
print(S.isIdealPermutation(A))
A = [1,2,0]
print(S.isIdealPermutation(A))
A = [2,1,0]
print(S.isIdealPermutation(A))