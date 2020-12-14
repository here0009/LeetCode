"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        wrong answer
        """
        def calc(d, str_n, sub_len):
            if sub_len < len(str_n):
                return 10**(sub_len-1)
            if d < str_n[0]:
                return 10**(sub_len-1)
            elif d == str_n[0]:
                return int(str_n[1:])
            return 10**(sub_len-2)

        def genNum(str_n, k, start):
            # print(str_n, k, start)
            if k == 0:
                return ''
            if k <= 10 and len(str_n) == 1:
                return digits[k-1]
            len_s = len(str_n)
            d = digits[start]
            sub_len = 1
            while k - calc(d, str_n, sub_len) > 0:
                # print(d, str_n, sub_len, k, start)
                k -= calc(d, str_n, sub_len)
                if sub_len == len_s:
                    sub_len = 1
                    start += 1

                    d = digits[start]
                else:
                    sub_len += 1
            return d + genNum(str_n[1:], k, 0)

        str_n = str(n)
        digits = '0123456789'

        return int(genNum(str_n, k, 1))


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        wrong answer
        """
        def calc(d, str_n):
            if d < str_n[0]:
                res = counts[len(str_n)]
            elif d == str_n[0]:
                res = int(str_n[1:]) + counts[len(str_n)-1] - (int(str_n) == 0)
            else:
                res = counts[len(str_n)-1]
            # print('d, str_n, res', d, str_n, res)
            return res

        def genNum(str_n, k, start):
            if k == 0:
                return ''
            if k <= 10 and len(str_n) == 1:
                return digits[k-(1-start)]
            d = digits[start]
            while k - calc(d, str_n) > 0:
                # print(d, str_n, k, start)
                k -= calc(d, str_n)
                start += 1
                d = digits[start]
            res = d + genNum(str_n[1:], k-1, 0) 
            # print('str_n, k, start, res',str_n, k, start, res)
            return res

        str_n = str(n+1)
        # get the numbers < n+1 , that is numbers <= n, judge with the equal condition is tricky
        digits = '0123456789'
        counts = [0]
        for i in range(11):
            counts.append(counts[-1] + 10**i)
        # print(counts)
        # counts[i] is the max total numbers which length of i
        return int(genNum(str_n, k, 1))


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans = 1
        k -= 1
        while k > 0:
            gap = self.findGap(n, ans, ans + 1)
            if gap <= k:
                ans += 1
                k -= gap
            else:
                ans *= 10
                k -= 1
        return ans

    def findGap(self, n, p, q):
        gap = 0
        while p <= n:
            gap += max(0, min(n + 1, q) - p)
            p *= 10
            q *= 10
        return gap


class Solution:
    def findKthNumber(self, n, k):
        def calc(start, end):
            res = 0
            while n >= start:
                res += max(0, min(n+1, end) - start)
                start *= 10
                end *= 10
            return res

        res = 1
        k -= 1
        while k > 0:
            counts = calc(res, res+1)
            if k >= counts:
                res += 1
                k -= counts
            else:
                res *= 10
                k -= 1
        return res

S = Solution()
n = 13
k = 2
print(S.findKthNumber(n, k))
n = 132
k = 33
print(S.findKthNumber(n, k))
# Output
# 119
# Expected
# 128
n = 100
k = 5
print(S.findKthNumber(n, k))
n = 10000
k = 10000
print(S.findKthNumber(n, k))
# Output
# 9996
# Expected
# 9999