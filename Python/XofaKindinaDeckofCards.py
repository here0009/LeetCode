"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
"""
from collections import Counter
class Solution_1:
    def hasGroupsSizeX(self, deck) -> bool:
        d_counter = Counter(deck)
        values_set = set(d_counter.values())
        if len(values_set) == 1:
            return values_set.pop() >= 2
        f = values_set.pop()
        s = values_set.pop()
        #find the min divider of first and second element of d_counter.values()
        if f > s:
            f,s = s,f
        min_divider = f+1
        for i in range(f,1,-1):
            if f%i == 0 and s%i == 0:
                min_divider = i
        if min_divider == f+1:
            return False
        for v in values_set:
            if v % min_divider != 0:
                return False
        return True

from functools import reduce
from collections import Counter
class Solution:
    """
    use reduce to write an elegant one
    """
    def hasGroupsSizeX(self, deck) -> bool:
        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a

        d_counter = Counter(deck)
        return reduce(gcd, d_counter.values()) > 1

s = Solution()
deck = [1,2,3,4,4,3,2,1]
print(s.hasGroupsSizeX(deck))
deck = [1,1,1,2,2,2,3,3]
print(s.hasGroupsSizeX(deck))
deck = [1]
print(s.hasGroupsSizeX(deck))
deck = [1,1]
print(s.hasGroupsSizeX(deck))
deck = [1,1,2,2,2,2]
print(s.hasGroupsSizeX(deck))
deck = [1,1,1,1,2,2,2,2,2,2]
print(s.hasGroupsSizeX(deck))

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
print(gcd(15,25))
print(gcd(25,15))