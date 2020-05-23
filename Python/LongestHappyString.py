"""
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def add(v,k):
            if v < -1:
                self.res += 2*k
                v += 2
            elif v == -1:
                self.res += k
                v += 1
            if v != 0:
                heapq.heappush(vals, [v,k])

        self.res = ''
        vals = []
        for k,v in zip(['a','b','c'], [a,b,c]):
            if v > 0:
                heapq.heappush(vals,[-v,k])
        # print(vals)
        while len(vals) > 1:
            v,k = heapq.heappop(vals)
            if len(self.res)>0 and self.res[-1] == k:
                v2,k2 = heapq.heappop(vals)
                # print('v',v,k,'v2',v2,k2)
                if v < v2:  
                    self.res += k2
                    v2 += 1
                    if v2 != 0:
                        heapq.heappush(vals,[v2,k2])
                else:
                    add(v2,k2)
                heapq.heappush(vals, [v,k])
            else:
                add(v,k)
                
        if vals:
            v,k = heapq.heappop(vals)
            if not self.res or self.res[-1] != k:
                add(v,k)
        return self.res



S = Solution()


a = 1
b = 1
c = 7
print(S.longestDiverseString(a,b,c))
a = 2
b = 2
c = 1
print(S.longestDiverseString(a,b,c))
a = 7
b = 1
c = 0
print(S.longestDiverseString(a,b,c))
a = 0
b = 8
c = 11
print(S.longestDiverseString(a,b,c))
# Output:
# "ccbbccbbccbbccbbcc"
# Expected:
# "ccbccbbccbbccbbccbc"
   # ccbccbbccbbccbbccbc