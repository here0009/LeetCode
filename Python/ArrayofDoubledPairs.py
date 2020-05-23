"""
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

 

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false
 

Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000
"""
from collections import Counter
class Solution_1:
    def canReorderDoubled(self, A) -> bool:
        A_counter = Counter(A)
        double_counter = dict()
        A = sorted(A, key = abs)
        for a in A:
            # print(A_counter)
            # print(double_counter)
            if a in double_counter and double_counter[a] > 0:
                double_counter[a] -= 1
            else:
                A_counter[a] -= 1
                b = 2*a
                if b not in A_counter or A_counter[b] < 0:
                    return False
                else:
                    A_counter[b] -= 1
                double_counter[b] = double_counter.get(b,0) + 1
        return True

from collections import Counter
class Solution:
    def canReorderDoubled(self, A) -> bool:
        A_counter = Counter(A)
        A = sorted(A, key = abs)
        for a in A:
            # print(a,A_counter)
            if A_counter[a] == 0:
                continue
            if A_counter[2*a] == 0:
                return False
            A_counter[a] -= 1
            A_counter[2*a] -= 1
        return True

from collections import Counter
class Solution:
    def canReorderDoubled(self, A) -> bool:
        A_counter = Counter(A)
        A_keys = sorted(A_counter.keys(), key = abs)
        for x in A_keys:
            if A_counter[x] > A_counter[2*x]:
                return False
            A_counter[2*x] -= A_counter[x] #it can still match with 4*x
        return True


s = Solution()
A = [3,1,3,6]
print(s.canReorderDoubled(A))
A = [2,1,2,6]
print(s.canReorderDoubled(A))
A = [4,-2,2,-4]
print(s.canReorderDoubled(A))
A = [1,2,4,16,8,4]
print(s.canReorderDoubled(A))

A = [2,1,2,1,1,1,2,2]
print(s.canReorderDoubled(A))