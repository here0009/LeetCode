"""
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
"""


from functools import lru_cache
from typing import Set, List
from math import sqrt
class UnionFind:
    def __init__(self):
        self.root = dict()
        self.size = dict()

    def find(self, v):
        if v not in self.root:
            self.root[v] = v
            self.size[v] = 0
        else:
            if v != self.root[v]:
                self.root[v] = self.find(self.root[v])
        return self.root[v]

    def union(self, p, q):
        rp, rq = self.find(p), self.find(q)
        if rq < rp:  # make p the smaller one
            rp, rq = rq, rp
        if rp == rq:
            return False
        self.root[rq] = rp
        self.size[rp] += self.size[rq]
        return True


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        """
        Thoughts: union all the prime factor of A, find the largest size
        TLE 96/100
        """
        @lru_cache(None)
        def primeFactors(a: int) -> Set[int]:
            """
            return the prime factors of a
            """
            res = set()
            if a < 2:
                return res
            if a == 2:
                return set([2])
            k = int(sqrt(a)) + 2
            for i in range(2, k):
                q, rmd = divmod(a, i)
                if rmd == 0:
                    if len(primeFactors(i)) == 1:
                        # print('i', i)
                        res.add(i)
                    if len(primeFactors(q)) == 1:
                        res.add(q)
            if not res:
                res.add(a)
            return res

        uf = UnionFind()
        for a in A:
            if a <= 1:
                continue
            factors = primeFactors(a)
            factor_roots = set(uf.find(v) for v in factors)
            # print(a, factors, factor_roots)
            p = factor_roots.pop()
            uf.size[p] += 1
            for q in factor_roots:

                uf.union(p, q)
            # print(uf.root, uf.size)
        return max(list(uf.size.values()) + [1])  # the min size of A is 1


M = 10**6 + 7
isPrime = [True] * M
isPrime[0], isPrime[1] = False, False
k = int(sqrt(M)) + 2
for i in range(2, k):
    if isPrime[i]:
        for j in range(i * i, M, i):
            isPrime[j] = False


class UnionFind:
    def __init__(self):
        self.root = dict()
        self.size = dict()

    def find(self, v):
        if v not in self.root:
            self.root[v] = v
            self.size[v] = 0
        else:
            if v != self.root[v]:
                self.root[v] = self.find(self.root[v])
        return self.root[v]

    def union(self, p, q):
        rp, rq = self.find(p), self.find(q)
        if rq < rp:  # make p the smaller one
            rp, rq = rq, rp
        if rp == rq:
            return False
        self.root[rq] = rp
        self.size[rp] += self.size[rq]
        return True

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        """
        try to use a list to store the information of prime
        """
        @lru_cache(None)
        def primeFactors(a: int) -> Set[int]:
            """
            return the prime factors of a
            """
            res = set()
            if isPrime[a]:
                return set([a])
            k = int(sqrt(a)) + 2
            for i in range(2, k):
                q, rmd = divmod(a, i)
                if rmd == 0:
                    if isPrime[i]:
                        res.add(i)
                    if isPrime[q]:
                        res.add(q)
            return res

        uf = UnionFind()
        for a in A:
            if a <= 1:
                continue
            factors = primeFactors(a)
            factor_roots = set(uf.find(v) for v in factors)
            # print(a, factors, factor_roots)
            p = factor_roots.pop()
            uf.size[p] += 1
            for q in factor_roots:

                uf.union(p, q)
            # print(uf.root, uf.size)
        return max(list(uf.size.values()) + [1])  # the min size of A is 1



from typing import Set, List
from math import sqrt
from collections import defaultdict
class UnionFind:
    def __init__(self, length):
        self.root = list(range(length))
        self.size = [1] * length

    def find(self, p):
        if p != self.root[p]:
            self.root[p] = self.find(self.root[p])
        return self.root[p]

    def union(self, p, q):
        rp, rq = self.find(p), self.find(q)
        if rq < rp:  # make p the smaller one
            rp, rq = rq, rp
        if rp == rq:
            return False
        self.root[rq] = rp
        self.size[rp] += self.size[rq]
        return True


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        """
        instead of calculate calculate primer factors for a in A.
        we can just append a to a list in a dict of the specific factor primes[p]: List[index], then union the elements in the list
        """
        def primeFactors(x):
            res = set()
            x = a
            for p in primes_numbers:
                if p * p > x:
                    break
                if x % p == 0:
                    res.add(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                res.add(x)
                primes_numbers.append(x)
            return res

        primes_numbers = []
        for x in range(2, int(max(A)**0.5)+1):
            for y in primes_numbers:
                if x % y == 0:
                    break
            else:
                primes_numbers.append(x)

        len_A = len(A)
        primes = defaultdict(list)
        for i, a in enumerate(A):
            if a <= 1:
                continue
            factors = primeFactors(a)
            for p in factors:
                primes[p].append(i)

        uf = UnionFind(len_A)
        for lst in primes.values():
            if len(lst) > 1:
                p = uf.find(lst[0])
                for q in lst[1:]:
                    uf.union(p, q)

        return max(uf.size + [1])  # the min size of A is 1

S = Solution()
A = [4,6,15,35]
print(S.largestComponentSize(A))
A = [20,50,9,63]
print(S.largestComponentSize(A))
A = [2,3,6,7,4,12,21,39]
print(S.largestComponentSize(A))
A = [3,10,11,76,29,81,74,59,24,52,58,15,42,30]
print(S.largestComponentSize(A))