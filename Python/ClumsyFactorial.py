"""
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.

 

Example 1:

Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1
Example 2:

Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
 

Note:

1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)
"""
class Solution_1:
    def helper(self, n):
        # print('n',n)
        if n <=2:
            return -1*n
        if n == 3:
            return -3*2//1
        if n == 4:
            return -4*3//2 - 1
        if n > 4:
            return n*(n-1)//(n-2)-(n-3)-self.helper(n-4)

    def clumsy(self, N: int) -> int:
        if N <=2:
            return N
        if N == 3:
            return 3*2//1
        if N == 4:
            return 4*3//2 + 1
        if N > 4:
            return N*(N-1)//(N-2)+(N-3)-self.helper(N-4)


class Solution:
    def clumsy(self, N: int) -> int:
        def helper(n):
            # print('n',n)
            if n > 2:
                return n*(n-1)//(n-2)
            elif n >= 1:
                return n
            else:
                return 0

        res = helper(N)
        N = N-3
        opt = 1
        while N > 0:
            # print('N',N)
            if opt % 2 == 1:
                res += N
                N -= 1
            else:
                res -= helper(N)
                N -= 3
            opt += 1
        return res




s = Solution()
# print(s.clumsy(4))
print(s.clumsy(10))
for i in range(1,13):
    print(i,s.clumsy(i))



