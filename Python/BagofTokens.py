"""
You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has potentially two ways to use it.

If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
Return the largest number of points we can have after playing any number of tokens.

 

Example 1:

Input: tokens = [100], P = 50
Output: 0
Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2
 

Note:

tokens.length <= 1000
0 <= tokens[i] < 10000
0 <= P < 10000
"""


from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens, P: int) -> int:
        tokens = sorted(tokens)
        dq = deque(tokens)
        res, points = 0, 0
        while dq and (P >= dq[0] or points):
            # print(dq, points, res, P)
            if P >= dq[0]:
                P -= dq.popleft()
                points += 1
            else:
                P += dq.pop()
                points -= 1
            res = max(res, points)
        return res

S = Solution()
tokens = [100]
P = 50
print(S.bagOfTokensScore(tokens, P))
tokens = [100,200]
P = 150
print(S.bagOfTokensScore(tokens, P))
tokens = [100,200,300,400]
P = 200
print(S.bagOfTokensScore(tokens, P))

