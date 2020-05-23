"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
from collections import defaultdict
from functools import lru_cache
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        """
        TLE
        """
        if not envelopes:
            return 0
        length = len(envelopes)
        path = defaultdict(list)
        for i in range(length-1):
            w1,h1 = envelopes[i]
            for j in range(i+1, length):
                w2,h2 = envelopes[j]
                if w1 < w2 and h1 < h2:
                    path[i].append(j)
                elif w1 > w2 and h1 > h2:
                    path[j].append(i)

        @lru_cache(None)
        def dfs(i):
            if not path[i]:
                return 1
            return 1+max(dfs(j) for j in path[i])

        self.res = 1
        for i in range(length):
            self.res =  max(self.res, dfs(i))
        return self.res


from collections import defaultdict
from functools import lru_cache
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        """
        TLE
        """
        if not envelopes:
            return 0
        length = len(envelopes)
        path = defaultdict(list)
        for i in range(length-1):
            w1,h1 = envelopes[i]
            for j in range(i+1, length):
                w2,h2 = envelopes[j]
                if w1 < w2 and h1 < h2:
                    path[i].append(j)
                elif w1 > w2 and h1 > h2:
                    path[j].append(i)

        print(path)
        @lru_cache(None)
        def dfs(i):
            if not path[i]:
                return 1
            return 1+max(dfs(j) for j in path[i])

        self.res = 1
        for i in range(length):
            self.res =  max(self.res, dfs(i))
        return self.res

from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes = sorted(envelopes, key = lambda x:[x[0], -x[1]])
        dolls = []
        for w,h in envelopes:
            index = bisect_left(dolls, h)
            if len(dolls) == index:
                dolls.append(h)
            else:
                dolls[index] = h #no increasement for res
        return len(dolls)



S = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(S.maxEnvelopes(envelopes))
envelopes = []
print(S.maxEnvelopes(envelopes))
