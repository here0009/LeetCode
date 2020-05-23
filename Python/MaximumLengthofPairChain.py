"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""
import bisect
class Solution:
    def findLongestChain(self, pairs) -> int:
        seconds = []
        pairs = sorted(pairs, key = lambda x:x[1])
        for f,s in pairs:
            index = bisect.bisect_left(seconds,f)
            if index == len(seconds):
                seconds.append(s)
            else:
                if s < seconds[index]:
                    seconds[index] = s
            # print(seconds)
        return len(seconds)

class Solution:
    def findLongestChain(self, pairs) -> int:
        pairs = sorted(pairs, key = lambda x:x[1])
        curr = float('-inf')
        res = 0
        for f,s in pairs:
            if curr < f:
                curr = s
                res += 1
        return res

s = Solution()
pairs = [[1,2], [2,3], [3,4]]
print(s.findLongestChain(pairs))

pairs = [[1,2]]
print(s.findLongestChain(pairs))

pairs = [[3,4],[2,3],[1,2]]
print(s.findLongestChain(pairs))