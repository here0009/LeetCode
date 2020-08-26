"""
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
 

Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9
"""


from collections import Counter
from collections import defaultdict
class Solution:
    def numSquarefulPerms(self, A) -> int:
        def dfs(num, index):
            if index == length-1:
                self.res += 1
            counter[num] -= 1
            for next_num in candidates[num]:
                if counter[next_num] > 0:
                    dfs(next_num, index+1)
            counter[num] += 1

        counter = Counter(A)
        candidates = defaultdict(set)
        length = len(A)
        for x in counter.keys():
            for y in counter.keys():
                if (int((x + y)**0.5))**2 == x + y:
                    candidates[x].add(y)
        # print(candidates)
        self.res = 0
        for num in counter:
            dfs(num, 0)
        return self.res

import collections
class Solution_1(object):
    def numSquarefulPerms(self, A):
        c, self.res = collections.Counter(A), 0
        can = {i : {j for j in c if (int((i + j) ** 0.5)) ** 2 == i + j} for i in c}
        print(can)
        def dfs(x, idx):
            c[x] -= 1
            if idx == len(A) - 1: self.res += 1
            for y in can[x]: 
                if c[y]: dfs(y, idx + 1)
            c[x] += 1
        for i in c: dfs(i, 0)
        return self.res

S = Solution()
print(S.numSquarefulPerms([1,17,8]))
print(S.numSquarefulPerms([2,2,2]))