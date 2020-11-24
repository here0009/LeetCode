"""
Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

 

Example 1:


Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.
 

Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-students-taking-exam
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from functools import lru_cache
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        @lru_cache(None)
        def dp(index, memo):
            """
            return the max student we can put until index, memo is the seat occupied of previous C seat
            """
            if index == R*C:
                return 0
            i, j = divmod(index, C)
            score = dp(index+1, memo[1:] + tuple(seats[i][j]))
            if (seats[i][j] != '.') or (j < C-1 and memo[2] == 1) or (j > 0 and (memo[-1] == 1 or memo[0] == 1)):
                return score
            else:
                return max(score, 1+dp(index+1, memo[1:]+tuple([1])))

        R, C = len(seats), len(seats[0])
        return dp(0, tuple([0]*(C+1)))


# 作者：z1m
# 链接：https://leetcode-cn.com/problems/maximum-students-taking-exam/solution/xiang-jie-ya-suo-zhuang-tai-dong-tai-gui-hua-jie-f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from functools import reduce
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0]),
        dp = [[0]*(1 << n) for _ in range(m+1)]  # 状态数组 dp
        a = [reduce(lambda x,y:x|1<<y,[0]+[j for j in range(n) if seats[i][j]=='#'])  for i in range(m)] # 将 # 设为 1，当遇到 . 时与运算结果为 0，表示可以坐人
        # print(a)
        for row in range(m)[::-1]: # 倒着遍历
            for j in range(1 << n):
                if not j & j<<1 and not j&j>>1 and not j & a[row]: # j & a[row]代表该位置可以坐人，j & j<<1 and not j&j>>1 表示该位置左右没人可以坐的
                    for k in range(1 << n):
                        if not j&k<<1 and not j&k>>1: # j状态的左上和右上没有人
                            dp[row][j] = max(dp[row][j], dp[row+1][k] + bin(j).count('1'))
        # print(dp)
        return max(dp[0])




S = Solution()
seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
print(S.maxStudents(seats))
seats = [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]
print(S.maxStudents(seats))
seats = [["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]
print(S.maxStudents(seats))