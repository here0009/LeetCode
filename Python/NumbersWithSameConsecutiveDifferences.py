"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9
"""
class Solution_1:
    """
    Wrong answer for testcase 5
    """
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]
        repeats, isOdd = divmod(N, 2)
        res_2d = set()
        for i in range(1,10):
            if i-K >= 0 and i-K < 10:
                res_2d.add(str(i*10 +i -K))
            if i+K >= 0 and i+K < 10:
                res_2d.add(str(i*10 + i + K))
        if isOdd:
            res = [int(s*repeats+s[0]) for s in res_2d]
        else:
            res = [int(s*repeats) for s in res_2d]
        return res

class Solution:
    """
    Wrong answer for testcase 5
    """
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]

        res_tmp = {str(i) for i in range(1,10)}
        while N > 1:
            res = set()
            for s in res_tmp:
                i = int(s[-1])
                if i-K >= 0 and i-K < 10:
                    res.add(s +str(i-K))
                if i+K >= 0 and i+K < 10:
                    res.add(s +str(i+K))
            res_tmp = res
            N-=1
        return [int(s) for s in res]

s = Solution()
print(s.numsSameConsecDiff(2, 1))
print(s.numsSameConsecDiff(3, 7))
print(s.numsSameConsecDiff(1, 1))
print(s.numsSameConsecDiff(2, 0))
print(s.numsSameConsecDiff(3, 1))
"""
TestCase 5
Input:
3
1
Output:
[898,323,545,454,565,212,101,676,767,878,989,232,787,434,121,343,656]
Expected:
[101,121,123,210,212,232,234,321,323,343,345,432,434,454,456,543,545,565,567,654,656,676,678,765,767,787,789,876,878,898,987,989]
"""

