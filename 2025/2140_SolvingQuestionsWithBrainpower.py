"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

 

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
 

Constraints:

1 <= questions.length <= 105
questions[i].length == 2
1 <= pointsi, brainpoweri <= 105
"""
from typing import List

class Solution_1: # wrong answer
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * (length + 1)
        # print('='*20)
        # print(questions)
        for i in range(1, length + 1):
            point, brain_power = questions[i-1]
            dp[i] = max(dp[i-1], dp[i] + point)
            extend_i = i + brain_power + 1
            if extend_i < length + 1:
                dp[extend_i] = max(dp[i], dp[extend_i])
            # print(i, dp)
        print(dp)
        return max(dp)


class Solution_2: # wrong answer
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        choose = [0] * (length + 1)
        no_choose = [0] * (length + 1)
        # print('='*20)
        # print(questions)
        for i in range(1, length + 1):
            point, brain_power = questions[i-1]
            choose[i] = choose[i] + point
            no_choose[i] = max(choose[i-1], no_choose[i-1])
            extend_i = i + brain_power + 1
            if extend_i < length + 1:
                choose[extend_i] = max(choose[i], no_choose[i], choose[extend_i])
            # print(i, dp)
        print(choose)
        print(no_choose)
        return max(choose + no_choose)
    
class Solution_3: # wrong answer
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * (length + 1)
        # print('='*20)
        # print(questions)
        for i in range(1, length + 1):
            point, brain_power = questions[i-1]
            dp[i] = max(dp[i-1], dp[i])
            extend_i = min(length, i + brain_power)
            dp[extend_i] = max(dp[i]+point, dp[extend_i])
            # print(i, dp)
        print(dp)
        return dp[length]

class Solution_4:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * (length + 1)
        for i in range(length):
            point, brain_power = questions[i]
            dp[i+1] = max(dp[i], dp[i+1])
            extend_i = min(length, i+brain_power+1)
            dp[extend_i] = max(dp[extend_i], dp[i]+point)
        return dp[length]


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * (length + 1)
        for i in range(length-1, -1, -1):
            point, brain_power = questions[i]
            j = min(length, i + 1 + brain_power)
            dp[i] = max(dp[i+1], dp[j] + point)
        return dp[0]



sol = Solution()
questions = [[3,2],[4,3],[4,4],[2,5]]
print(sol.mostPoints(questions))
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(sol.mostPoints(questions))
questions = [[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]] 
print(sol.mostPoints(questions)) # res: 781