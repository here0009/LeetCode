"""
Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
"""


class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        """
        TLE
        """
        res = 0
        length = len(arr1)
        for i in range(length-1):
            for j in range(i+1, length):
                res = max(res, abs(arr1[i]-arr1[j]) + abs(arr2[i]-arr2[j]) + abs(i-j))
                # print(i,j,res)
        return res


class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        """
        wrong answer
        """
        minv, maxv = float('inf'), float('-inf')
        res = float('-inf')
        length = len(arr1)
        for a1,a2,i in zip(arr1, arr2, range(length)):
            lst = [a1+a2+i, a1-a2+i, -a1-a2+i, a2-a1+i]
            min_lst, max_lst = min(lst), max(lst)
            res = max(maxv - min_lst, max_lst - minv, res)
            minv, maxv = min(minv, min_lst), max(maxv, max_lst)
        return res


class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        res = 0
        length = len(arr1)
        for p, q in [(1,1),(-1,-1),(1,-1),(-1,1)]:
            min_v = p*arr1[0] + q*arr2[0] + 0
            for i in range(1, length):
                v = p*arr1[i] + q*arr2[i] + i
                res = max(res, v - min_v)
                min_v = min(v, min_v)
        return res

S = Solution()
arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]
print(S.maxAbsValExpr(arr1, arr2))

arr1 = [1,-2,-5,0,10]
arr2 = [0,-2,-1,-7,-4]
print(S.maxAbsValExpr(arr1, arr2))
