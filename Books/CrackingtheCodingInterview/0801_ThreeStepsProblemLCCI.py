"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [0, 1, 2, 4]
        M = 10**9 + 7
        for i in range(4, n + 1):
            dp.append(sum(dp[i - 3:]) % M)
        return dp[n]


class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [0, 1, 2, 4]
        M = 10**9 + 7
        if n < 4:
            return dp[n]
        a, b, c = dp[1:]
        for i in range(4, n + 1):
            a, b, c = b, c, (a + b + c) % M
        return c


S = Solution()
print(S.waysToStep(3))
print(S.waysToStep(5))

all_xray_df[all_xray_df['Pneumonia']  == True].apply(lambda x:
    os.popen(r'copy {} {}{}.format(x['path'], ,'.\test', x['Image Index']))