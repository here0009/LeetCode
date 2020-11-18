"""
You are given an even number of people num_people that stand around a circle and each person shakes hands with someone else, so that there are num_people / 2 handshakes total.

Return the number of ways these handshakes could occur such that none of the handshakes cross.

Since this number could be very big, return the answer mod 10^9 + 7

 

Example 1:

Input: num_people = 2
Output: 1
Example 2:



Input: num_people = 4
Output: 2
Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and the second one is [(2,3),(4,1)].
Example 3:



Input: num_people = 6
Output: 5
Example 4:

Input: num_people = 8
Output: 14
 

Constraints:

2 <= num_people <= 1000
num_people % 2 == 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/handshakes-that-dont-cross
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n <= 2:
                return 1
            n -= 2
            res = 0
            for i in range(0, n+1, 2):
                res = (res + dp(i)*dp(n-i)) % M
            return res
        M = 10**9 + 7
        return dp(num_people)

S = Solution()
for i in range(2, 11, 2):
    print(i, S.numberOfWays(i))