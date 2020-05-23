"""
Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :

p[0] = start
p[i] and p[i+1] differ by only one bit in their binary representation.
p[0] and p[2^n -1] must also differ by only one bit in their binary representation.
 

Example 1:

Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: The binary representation of the permutation is (11,10,00,01). 
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
Example 2:

Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).
 

Constraints:

1 <= n <= 16
0 <= start < 2 ^ n
"""
"""
generate 01 permuatation only differ by 1, then find start, make it as the beginning of the res list
parent 0: left 0, right 1
parent 1: left 1, right 0
"""
class Solution:
    def circularPermutation(self, n: int, start: int):
        bfs = ['']
        while n > 0:
            bfs2 = []
            for i,v in enumerate(bfs):
                if i % 2 == 0: #even
                    bfs2.extend([v+'0', v+'1'])
                else:
                    bfs2.extend([v+'1', v+'0'])
            bfs = bfs2
            n -= 1

        res_int = [int(s,2) for s in bfs]
        for i in range(len(res_int)):
            if res_int[i] == start:
                return res_int[i:] + res_int[:i]
        return res_int

s = Solution()
n = 2
start = 3
print(s.circularPermutation(n, start))

n = 3
start = 2
print(s.circularPermutation(n, start))