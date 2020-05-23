"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
class Solution_1:
    def countBits(self, num: int):
        res = []
        for i in range(num+1):
            res.append(sum([int(j) for j in bin(i)[2:]]))
        return res

class Solution_2:
    def countBits(self, n: int):
        res = [0]
        for i in range(1,n+1):
            res.append(res[i//2]+i%2)
        return res

class Solution:
    def countBits(self, n: int):
        """
        i&i-1 drops the lowest 1, 14 & 13 => 1110 & 1101 => 1100 => 10, so we can calculate 14 based on 10.
        """
        res = [0]*(n+1)
        for i in range(1,n+1):
            res[i] = res[i&(i-1)]+1
        return res

s = Solution()
num = 5
print(s.countBits(num))
num = 1
print(s.countBits(num))