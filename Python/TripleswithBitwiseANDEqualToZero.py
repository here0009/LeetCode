"""
Given an array of integers A, find the number of triples of indices (i, j, k) such that:

0 <= i < A.length
0 <= j < A.length
0 <= k < A.length
A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
 

Example 1:

Input: [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2
 

Note:

1 <= A.length <= 1000
0 <= A[i] < 2^16
"""
"""
Thoughts:
3 cases
1. 0 & 0 = 0, Counter[0]
2. 10 & 01 = 0, Counter[0]*Counter[1]*3*2*2, last 2 for 1 and 2 can switch the place
3. 101 & 110 & 011 = 0, Counter[3]*Counter[4]*Counter[5]*3*2
"""
from collections import Counter
class Solution:
    def countTriplets(self, A) -> int:
        n = len(A)
        counter_A = Counter(A)
        res = 0
        counter_A_key_list = sorted(list(counter_A.keys()))
        len_keys = len(counter_A_key_list)
        total = n**3
        #case 2
        for i in range(len_keys):
            k1 = counter_A_key_list[i]
            v1 = counter_A[k1]
            print(k1,v1,res)
            if k1 == 0:
                print('total', total)
                print('n-v1',(n-v1)**3)
                n -= v1
                res += total - n**3
            else:
                for j in range(i+1, len_keys):
                    k2 = counter_A_key_list[j]
                    v2 = counter_A[k2]
                    # n = 
                    if k1&k2 == 0:
                        res += total - (n-v1-v2)**3
                    else:
                        for l in range(j+1, len_keys):
                            k3 = counter_A_key_list[l]
                            v3 = counter_A[k3]
                            if k1&k2&k3 == 0:
                                res += v1*v2*v3*6
        return res

from collections import Counter
class Solution:
    def countTriplets(self, A) -> int:
        """
        wrong answer
        """
        n = len(A)
        counter_A = Counter(A)
        res = 0
        counter_A_key_list = sorted(list(counter_A.keys()))
        len_keys = len(counter_A_key_list)
        total = n**3
        #case 2
        for i in range(len_keys):
            k1 = counter_A_key_list[i]
            v1 = counter_A[k1]
            # print(k1,v1,res)
            if k1 == 0: #exclude 0 first
                n -= v1
                res += total - n**3
            else:
                for j in range(i+1, len_keys):
                    k2 = counter_A_key_list[j]
                    v2 = counter_A[k2]
                    if k1&k2 == 0:
                        if n == 2:
                            res += 6
                        else:
                            res += 12*v1*v2 #enumerate(2,3)
                    else:
                        for l in range(j+1, len_keys):
                            k3 = counter_A_key_list[l]
                            v3 = counter_A[k3]
                            if k1&k2&k3 == 0:
                                res += v1*v2*v3*6
        return res


from collections import Counter
class Solution:
    def countTriplets(self, A) -> int:
        """
        wrong answer
        """
        n = len(A)
        counter_A = Counter(A)
        res = 0
        counter_A_key_list = sorted(list(counter_A.keys()))
        len_keys = len(counter_A_key_list)
        total = n**3
        #case 2
        for i in range(len_keys):
            k1 = counter_A_key_list[i]
            v1 = counter_A[k1]
            # print(k1,v1,res)
            if k1 == 0: #exclude 0 first
                n -= v1
                res += total - n**3
            else:
                for j in range(i+1, len_keys):
                    k2 = counter_A_key_list[j]
                    v2 = counter_A[k2]
                    if k1&k2 == 0:
                        if n == 2:
                            res += 6
                        else:
                            res += 12*v1*v2 #enumerate(2,3)
                    else:
                        for l in range(j+1, len_keys):
                            k3 = counter_A_key_list[l]
                            v3 = counter_A[k3]
                            if k1&k2&k3 == 0:
                                res += v1*v2*v3*6
        return res

from functools import lru_cache
class Solution:
    def countTriplets(self, A) -> int:
        @lru_cache(None)
        def dfs(counts, num):
            # print('counts,num',counts,num)
            if counts == 3:
                return num == 0
            res = 0
            for a in A:
                res += dfs(counts+1, num&a)
            return res

        res = 0
        for a in A:
            res += dfs(1,a)
        return res

from functools import lru_cache
class Solution:
    def countTriplets(self, A) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dfs(counts, num):
            # print(counts,num)
            if counts == 3:
                return num == 0
            if num == 0:
                if counts == 2:
                    return length #the last num could be any
                elif counts == 1:
                    return length**2 #the last two nums could be any

            res = 0
            for a in A:
                res += dfs(counts+1, num&a)
            return res

        length = len(A)
        res = 0
        for a in A:
            res += dfs(1,a)
        return res

from collections import Counter
class Solution:
    def countTriplets(self, A) -> int:
        dp = Counter(A)
        for i  in range(2):
            dp2 = Counter()
            for a in A:
                for key,val in dp.items():
                    dp2[key&a] += val
            dp = dp2
        return dp[0]

class Solution:
    def countTriplets(self, A):
            d = collections.defaultdict(int)
            for a in A:
                for b in A: d[a&b] += 1
            ans = 0
            for c in A:
                for ab in d:
                    if ab & c == 0: ans += d[ab]
            return ans

class Solution:
    def countTriplets(self, A):
        length = len(A)
        res = 0
        for i in range(length):
            for j in range(i,length):
                for k in range(j,length):
                    if A[i] & A[j] & A[k] == 0:
                        if i == j and j == k:
                            res += 1
                        elif i == j or j == k or i == k:
                            res += 3
                        else:
                            res += 6
        return res

S = Solution()
A = [2,1,3]
print(S.countTriplets(A))

A = [0,0,0,0]
print(S.countTriplets(A))

A = [3,6,5]
print(S.countTriplets(A))

A = [0]
print(S.countTriplets(A))                  

A = [4,1,0]
print(S.countTriplets(A))

A = [4,13,10,12]
print(S.countTriplets(A))
