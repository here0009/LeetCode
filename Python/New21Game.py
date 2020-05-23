"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
"""
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W : 
            return 1
        dp = [1] + [0]*N 
        Wsum = 1
        res = 0
        for i in range(1,N+1):
            dp[i] = Wsum/W
            if i < K:
                Wsum += dp[i]
            else:
                res += dp[i]
            if i - W >= 0:
                Wsum -= dp[i-W] #if W equals to 10, we can directly  get a 10 with a prob 1/10, but in the next round we can not get 11 directly, so we need to minus dp[0] == 1 from Wsum
        # total = 0
        # string = '{}\t{:.2f}\t{:.2f}'
        # for i in range(1,N+1):
        #     total += dp[i]
        #     print(string.format(i, dp[i], total))
        return res

s = Solution()
# print(s.new21Game(10,1,10))
# print(s.new21Game(6,1,10))  
print(s.new21Game(21,17,10))  