"""
为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。

为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。

示例 1：

输入：jump = [2, 5, 1, 1, 1, 1]

输出：3

解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。

限制：

1 <= jump.length <= 10^6
1 <= jump[i] <= 10000
"""
from functools import lru_cache
class Solution:
    def minJump(self, jump) -> int:
        left, right = 0,0
        res = 1
        length = len(jump)
        while left < length and right < length:
            # print(left, right)
            next_left = right+1
            next_right = max([jump[i]+i for i in range(left,right+1)])
            res += 1
            left, right = next_left, next_right
            if left > right:
                left, right = right, left
        # print(left,right)
        return res

from collections import deque    
class Solution:
    def minJump(self, jump) -> int:
        length = len(jump)
        visited = [0]*length
        q = deque([(0,0)])
        visited[0] = 1
        left = 0
        while q:
            curr, step = q.popleft()
            right = curr + jump[curr]
            if right >= length:
                return step+1
            if not visited[right]:
                q.append((right,step+1))
                visited[right] = 1
            for i in range(left+1, curr):
                if not visited[i]:
                    q.append((i,step+1))
                    visited[i] = 1
            left = max(left, curr)
        return -1

class Solution:
    def minJump(self, jump) -> int:
        visit = [0 for _ in range(len(jump))]
        q = [(0, 0)]
        visit[0] = 1

        max_left_idx = 0
        # BFS遍历
        while q:
            cur_idx, count = q.pop(0)
            right_idx = cur_idx + jump[cur_idx]

            if right_idx >= len(jump):
                return count + 1
            else:
                if not visit[right_idx]:
                    q.append((right_idx, count + 1))
                    visit[right_idx] = 1

            for i in range(max_left_idx+1, cur_idx):
                if not visit[i]:
                    q.append((i, count + 1))
                    visit[i] = 1

            max_left_idx = max(cur_idx, max_left_idx)
        return -1


S = Solution()
jump = [2, 5, 1, 1, 1, 1]
print(S.minJump(jump))


