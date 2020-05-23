"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        TLE
        """
        res = 0
        r = 1
        bulbs = [1]*n
        while r < n: #r+1 is the round number, start from round 2
            for i in range(r,n,r+1): 
                bulbs[i] = 1 - bulbs[i]
            r += 1
            # print(bulbs)
        return sum(bulbs)

from math import sqrt
class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Thoughts: a bulb is on if it is toggled odd times, 
        for a natural number n, it have 2*p divisors except n == k*k (k is also a natural number)
        e.g: 12 = 1*12, 2*6, 3*4 and 25 = 1*25, 5*5
        so only square numbers will be toggled odd times.
        the square number in n is sqrt(n)
        """
        return int(sqrt(n))

S = Solution()
n = 3
print(S.bulbSwitch(n))

n = 9999999
print(S.bulbSwitch(n))
