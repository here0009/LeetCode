"""
Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4-keys-keyboard
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def maxA(self, N: int) -> int:
        """
        TLE
        """
        bfs = [(0,0,0)]
        seen = set(bfs)
        res = 0
        while N >= 0:
            bfs2 = []
            # print(N, bfs)
            for p, s, c in bfs:
                res = max(res, p)
                for i,j,k in [(p+1, s, c), (p+c, s, c), (p, p, c), (p, s, s)]:
                    if (i,j,k) not in seen:
                        seen.add((i,j,k))
                        bfs2.append((i,j,k))
            bfs = bfs2
            N -= 1
        return res


from functools import lru_cache
class Solution:
    def maxA(self, N: int) -> int:
        def dfs(n, p, s, c):
            total = sum([p, s, c])
            if total < dp[n]:
                return
            dp[n] = max(dp[n], total - min([p,s,c]))
            if n == N:
                self.res = max(self.res, p)
                return
            dfs(n+1, p+max(c,1), s, c)
            dfs(n+1, p, max(s,p), c)
            dfs(n+1, p, s, max(s,c))

        self.res = 0
        dp = [0]*(N+1)
        dfs(0, 0, 0, 0)
        return self.res


# 作者：jhhuang
# 链接：https://leetcode-cn.com/problems/4-keys-keyboard/solution/qing-xi-pythondong-tai-gui-hua-by-jhhuang/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def maxA(self, N: int) -> int:
        # 最后一次按键要么是 A 要么是 C-V
        # 定义：dp[i] 表示 i 次操作后最多能显示多少个 A
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            # 按A键
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                # 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
                # j 之前的 2 个操作是 C-A C-C
                # 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[N]



S = Solution()
print(S.maxA(3))
print(S.maxA(7))
print(S.maxA(29))