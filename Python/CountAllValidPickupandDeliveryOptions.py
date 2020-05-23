"""
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90
 

Constraints:

1 <= n <= 500
"""

"""
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516968/JavaC%2B%2BPython-Easy-and-Concise

Intuition 1
Assume we have already n - 1 pairs, now we need to insert the nth pair.
To insert the first element, there are n * 2 - 1 chioces of position。
To insert the second element, there are n * 2 chioces of position。
So there are (n * 2 - 1) * n * 2 permutations.
Considering that delivery(i) is always after of pickup(i), we need to divide 2.
So it's (n * 2 - 1) * n.


Intuition 2
We consider the first element in all 2n elements.
The first must be a pickup, and we have n pickups as chioce.
It's pair can be any positino in the rest of n*2-1 positions.
So it's (n * 2 - 1) * n.


Intuition 3
The total number of all permutation obviously eauqls to 2n!.
For each pair, the order is determined, so we need to divide by 2.
So the final result is (2n)!/(2^n)


Complexity
For each run, Time O(N), Space O(1).
Also we can cache the result, so that O(1) amortized for each n.
But in doesn't help in case of LC.
Also we can pre calculate all results, so that we have O(N) space and O(1) time.
"""
class Solution:
    def countOrders(self, n: int) -> int:
        """
        k = 2*(n-1)
        f(n) = f(n-1)*(combination(k+1,1)+combination(k+1,2))
        """

        def f(n):
            # print(n)
            if n <= 1:
                return n
            else:
                k = 2*(n-1)
                return f(n-1)*((k+1) + (k+1)*k//2)

        M = 10**9+7
        return f(n) % M

class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        k = 1
        while k < n:
            res = res*((2*k+1) + (2*k+1)*k)
            k += 1
        M = 10**9+7
        return res % M

S = Solution()
for i in range(10):
    print(i,S.countOrders(i)) 
