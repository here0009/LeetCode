"""
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
Example 2:

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
Example 3:

Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
 

Constraints:

1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 106
1 <= ages[i] <= 1000
"""


class Solution:
    """
    TLE
    """
    def bestTeamScore(self, scores, ages) -> int:
        def dfs(status, index):
            if index == length:
                self.res = max(self.res, sum(players[i][0] for i in range(length) if status[i] == '1'))
                # print(status, index, self.res)
                return
            
            score, age = players[index]
            dfs(status+'0', index+1)
            status2 = list(status)
            # print('++++++++++')
            # print(score, age, status2, index)
            for i in range(index):
                if players[i][1] >= age:
                    break
                if status2[i] == '1' and players[i][0] > score:
                    status2[i] = '0'
            # print(status2, index)
            # print('++++++++++')
            dfs(''.join(status2)+'1', index+1)



        players = sorted(zip(scores, ages), key=lambda x:x[1])
        # print(players)
        length = len(players)
        self.res = 0
        dfs('', 0)
        return self.res


class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        players = sorted(zip(ages, scores))
        # length = len(players)
        dp = {0:0} # dp[v] record the max score we can get, for the max score smaller than v
        for _, score in players:
            res = 0
            for k,v in dp.items():
                if k <= score:
                    res = max(res, v+score)
            dp[score] = res
        # print(players)
        # print(dp)
        return max(dp.values())


class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        players = sorted(zip(ages, scores))
        length = len(players)
        dp = [0]*length
        for i in range(length):
            score = players[i][1]
            dp[i] = score
            for j in range(i):
                if players[j][1] <= score:
                    dp[i] = max(dp[i], score+dp[j])
        return max(dp)
S = Solution()
scores = [1,3,5,10,15]
ages = [1,2,3,4,5]
print(S.bestTeamScore(scores, ages))
scores = [4,5,6,5]
ages = [2,1,2,1]
print(S.bestTeamScore(scores, ages))
scores = [1,2,3,5]
ages = [8,9,10,1]
print(S.bestTeamScore(scores, ages))