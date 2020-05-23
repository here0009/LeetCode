"""
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181
 

Constraints:

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15

"""
class Solution_1:
    def dieSimulator(self, n: int, rollMax) -> int:
        N = len(rollMax)
        dp = [0]*N
        n -= 1
        for i in range(N):
            if rollMax[i] > 0:
                dp[i] = 1
                rollMax[i] -= 1
        print(dp)
        while n > 0:
            sum_dp = sum([dp[i] if rollMax[i] > 0 else 0])
            dp2 = [0]*N
            for i in range(N):
                if rollMax[i] > 0:
                    dp2[i] = sum_dp
                    rollMax[i] -= 1
                else:
                    dp2[i] = sum_dp - dp[i]
                # else:
            dp = dp2
            print(dp)
            print(rollMax)
            n -= 1
            
        return sum(dp)


class Solution_2:
    def dieSimulator(self, n: int, rollMax) -> int:
        """
        TLE for python
        """
        def dfs(k, index, rolls):
            """
            already got k*index, still need rolls, try bottom up soltuion
            """
            if rolls == 0:
                return 1
            if (k,index,rolls) in memo:
                return memo[(k,index,rolls)]
            res = 0
            for i in range(N):
                if i != index:
                    res += dfs(1,i,rolls-1)
                else:
                    if k < rollMax[index]:
                        res += dfs(k+1,i,rolls-1)
            res = res % M
            memo[(k,index,rolls)] = res 
            return res

        N = len(rollMax)
        M = 10**9+7
        memo = dict()
        res = dfs(0,0,n) #got nothing, needs n rolls
        # print(memo)
        return res


class Solution:
    def dieSimulator(self, n: int, rollMax) -> int:
        #dp[i][k] stands for the sequence ends with k consecutive i
        N = len(rollMax)
        M = 10**9+7
        Kmax = 17
        dp = [[0,1]+[0]*15 for _ in range(N)]
        # print(dp)
        while n > 1:
            dp2 = [[0]*Kmax for _ in range(N)]
            for i in range(N):
                for k in range(1,rollMax[i]+1):
                    for j in range(N):
                        if i != j:
                            dp2[j][1] += dp[i][k] % M
                        elif k < rollMax[i] :
                            dp2[i][k+1] += dp[i][k] % M
            dp = dp2
            n -= 1
        return sum(sum(row) for row in dp) % M


s = Solution()
n = 2
rollMax = [1,1,2,2,2,3]
print(s.dieSimulator(n, rollMax))

n = 2
rollMax = [1,1,1,1,1,1]
print(s.dieSimulator(n, rollMax))

n = 3
rollMax = [1,1,1,2,2,3]
print(s.dieSimulator(n, rollMax))

n = 5000
rollMax = [13,3,12,14,11,11]
print(s.dieSimulator(n, rollMax))