"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
"""
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_num = int(math.sqrt(c))+1
        for a in range(max_num):
            left,right = a,max_num
            tmp_min = a**2*2
            if tmp_min > c:
                break
            while left <= right:
                mid = (left+right)//2
                k = a**2 + mid**2
                if k < c:
                    left = mid+1
                elif k > c:
                    right = mid-1
                else:
                    print('{}^2+{}^2 = {}'.format(a,mid,c))
                    return True
        return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        i = 0
        while i**2 <= c:
            squares.add(i**2)
            i += 1
        # print(squares)
        for s in squares:
            if c - s in squares:
                # print(c,c-s)
                return True
        return False


import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_num = int(math.sqrt(c))+1
        for a in range(max_num):
            k = c - a**2
            b = int(math.sqrt(k))
            if b**2 == k:
                print('{}^2+{}^2 = {}'.format(a,b,c))
                return True
        return False

s = Solution()
c = 5
print(s.judgeSquareSum(c))

c = 4
print(s.judgeSquareSum(c))

# for i in range(100,200,10):
#     print(s.judgeSquareSum(i))

c = 2389
print(s.judgeSquareSum(c))

c = 16643588
print(s.judgeSquareSum(c))

c = 1759309629
print(s.judgeSquareSum(c))