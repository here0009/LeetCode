"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def backtrack(curr):
            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i in range(1,n+1):
                if i not in curr:
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()


        res = []
        for i in range(1,n+1):
            backtrack([i])
        return ''.join([str(i) for i in res[k-1]])


s = Solution()
n = 4
k = 9
print(s.getPermutation(n,k))

n = 3
k = 3
print(s.getPermutation(n,k))

n = 9
k = 94626
print(s.getPermutation(n,k))
