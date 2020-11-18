"""
You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.

You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.

The happiness of each person is calculated as follows:

Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.

 

Example 1:


Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
Output: 240
Explanation: Assume the grid is 1-indexed with coordinates (row, column).
We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
- Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
- Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
- Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
The grid happiness is 120 + 60 + 60 = 240.
The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.
Example 2:

Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
Output: 260
Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
- Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
- Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
- Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
The grid happiness is 90 + 80 + 90 = 260.
Example 3:

Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
Output: 240
 

Constraints:

1 <= m, n <= 5
0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
"""


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        """
        TLE
        """
        def inRange(i,j):
            return 0 <= i < m and 0 <= j < n

        def dfs(happiness, intro, extro):
            self.res = max(self.res, happiness)
            # print(happiness, intro, extro)
            # for row in maxtrix:
            #     print(row)
            if intro == 0 and extro == 0:
                return
            for i in range(m):
                for j in range(n):
                    if maxtrix[i][j] == 0:
                        neighbors = 0
                        diff = 0
                        for di,dj in dir4:
                            ni, nj = i+di, j+dj
                            if inRange(ni, nj) and maxtrix[ni][nj] != 0:
                                neighbors += 1
                                if maxtrix[ni][nj] == 1:
                                    diff -= 30
                                elif maxtrix[ni][nj] == 2:
                                    diff += 20
                        if intro > 0:
                            maxtrix[i][j] = 1
                            dfs(happiness+diff+120-30*neighbors, intro-1, extro)
                            maxtrix[i][j] = 0
                        if extro > 0:
                            maxtrix[i][j] = 2
                            dfs(happiness+diff+40+20*neighbors, intro, extro-1)
                            maxtrix[i][j] = 0

        dir4 = [(0,1), (0,-1), (1,0), (-1,0)]
        maxtrix = [[0]*n for _ in range(m)]
        self.res = 0
        dfs(0, introvertsCount, extrovertsCount)
        return self.res



# 作者：zerotrac2
# 链接：https://leetcode-cn.com/problems/maximize-grid-happiness/solution/zui-da-hua-wang-ge-xing-fu-gan-by-zerotrac2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, nx: int, wx: int) -> int:
        # 如果 x 和 y 相邻，需要加上的分数
        def calc(x: int, y: int) -> int:
            if x == 0 or y == 0:
                return 0
            # 例如两个内向的人，每个人要 -30，一共 -60，下同
            if x == 1 and y == 1:
                return -60
            if x == 2 and y == 2:
                return 40
            return -10
        
        n3 = 3**n
        # 预处理：每一个 mask 的三进制表示
        mask_span = dict()
        # 预处理：每一个 mask 去除最高位、乘 3、加上新的最低位的结果
        truncate = dict()

        # 预处理
        highest = n3 // 3
        for mask in range(n3):
            mask_tmp = mask
            bits = list()
            for i in range(n):
                bits.append(mask_tmp % 3)
                mask_tmp //= 3
            # 与方法一不同的是，这里需要反过来存储，这样 [0] 对应最高位，[n-1] 对应最低位
            mask_span[mask] = bits[::-1]
            truncate[mask] = [
                mask % highest * 3,
                mask % highest * 3 + 1,
                mask % highest * 3 + 2,
            ]
        
        # dfs(位置，轮廓线上的 mask，剩余的内向人数，剩余的外向人数)
        @lru_cache(None)
        def dfs(pos: int, borderline: int, nx: int, wx: int):
            # 边界条件：如果已经处理完，或者没有人了
            if pos == m * n or nx + wx == 0:
                return 0
            
            x, y = divmod(pos, n)
            
            # 什么都不做
            best = dfs(pos + 1, truncate[borderline][0], nx, wx)
            # 放一个内向的人
            if nx > 0:
                best = max(best, 120 + calc(1, mask_span[borderline][0]) \
                                     + (0 if y == 0 else calc(1, mask_span[borderline][n - 1])) \
                                     + dfs(pos + 1, truncate[borderline][1], nx - 1, wx))
            # 放一个外向的人
            if wx > 0:
                best = max(best, 40 + calc(2, mask_span[borderline][0]) \
                                    + (0 if y == 0 else calc(2, mask_span[borderline][n - 1])) \
                                    + dfs(pos + 1, truncate[borderline][2], nx, wx - 1))

            return best
        
        return dfs(0, 0, nx, wx)

# https://leetcode.com/problems/maximize-grid-happiness/discuss/936081/C%2B%2B-5D-DP

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def calc_cost(r, c, in_mask, ex_mask, d):
            ans, up = 0, (1 << (n - 1))
            if c > 0 and (in_mask & 1):
                ans += d - 30
            if r > 0 and (in_mask & up):
                ans += d - 30
            if c > 0 and (ex_mask & 1):
                ans += d + 20
            if r > 0 and (ex_mask & up):
                ans += d + 20
            return ans
        
        @lru_cache(None)
        def dp(idx, in_mask, ex_mask, in_cnt, ex_cnt):
            r, c = divmod(idx, n)
            if r >= m:
                return 0
            n_in_mask = (in_mask << 1) & ((1 << n) - 1)
            n_ex_mask = (ex_mask << 1) & ((1 << n) - 1)
            ans = dp(idx + 1, n_in_mask, n_ex_mask, in_cnt, ex_cnt)
            if in_cnt > 0:
                cur = 120 + calc_cost(r, c, in_mask, ex_mask, -30)
                ans = max(ans, cur + dp(idx + 1, n_in_mask + 1, n_ex_mask, in_cnt - 1, ex_cnt))
            if ex_cnt > 0:
                cur = 40 + calc_cost(r, c, in_mask, ex_mask, 20)
                ans = max(ans, cur + dp(idx + 1, n_in_mask, n_ex_mask + 1, in_cnt, ex_cnt - 1))
            return ans
        return dp(0, 0, 0, introvertsCount, extrovertsCount)


# https://leetcode.com/problems/maximize-grid-happiness/discuss/936467/Python-Short-and-clean-dp-with-diagram-expained
class Solution:
    def getMaxGridHappiness(self, m, n, I, E):
        InG, ExG, InL, ExL = 120, 40, -30, 20
        fine = [[0, 0, 0], [0, 2*InL, InL+ExL], [0, InL+ExL, 2*ExL]]
        
        @lru_cache(None)
        def dp(index, row, I, E):
            if index == -1: return 0

            R, C, ans = index//n, index%n, []
            neibs = [(1, I-1, E, InG), (2, I, E-1, ExG), (0, I, E, 0)]  
            
            for val, dx, dy, gain in neibs:
                tmp = 0
                if dx >= 0 and dy >= 0:
                    tmp = dp(index-1, (val,) + row[:-1], dx, dy) + gain
                    if C < n-1: tmp += fine[val][row[0]]  #right neighbor
                    if R < m-1: tmp += fine[val][row[-1]] #down neighbor
                ans.append(tmp)

            return max(ans)
        
        if m < n: m, n = n, m
            
        return dp(m*n-1, tuple([0]*n), I, E)

def getMaxGridHappiness(self, R: int, C: int, introvertsCount: int, extrovertsCount: int) -> int:

    @functools.lru_cache(None)
    def helper(i, memory, intros, extros):
        if intros == extros == 0 or i == R * C:
            return 0
        
        up, left = memory[0], memory[-1]

        # leave room blank (unless the number of empty rooms equals the number of people remaining)
        best = helper(i+1, memory[1:] + tuple([0]), intros, extros) if (N - (i - 1) >= intros + extros) else 0

        # add an introvert
        j = i % C
        if intros:
            score = 120 + score_map[(up, 1)] + bool(j) * score_map[(left, 1)]
            best = max(best, score + helper(i+1, memory[1:] + tuple([1]), intros - 1, extros))

        # add an extrovert
        if extros:
            score = 40 + score_map[(up, 2)] + bool(j) * score_map[(left, 2)]
            best = max(best, score + helper(i+1, memory[1:] + tuple([2]), intros, extros - 1))

        return best

    score_map = {(0, 1): 0,         # empty neighbor (0) add introvert (1) to current cell
                 (0, 2): 0,         # empty neighbor (0) add extrovert (2) to current cell
                 (1, 1): -30 - 30,  # introvert neighbor (1) add introvert (1) to current cell
                 (2, 1): 20 - 30,   # extrovert neighbor (2) add introvert (1) to current cell
                 (1, 2): -30 + 20,  # introvert neighbor (1) add extrovert (2) to current cell
                 (2, 2): 20 + 20}   # extrovert neighbor (2) add extrovert (2) to current cell

    N = R * C
    C, R = sorted((R, C))
    memory = tuple([0 for _ in range(C)])
    return helper(0, memory, introvertsCount, extrovertsCount)



from functools import lru_cache
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        """
        Thought: the score of current position is only relevant to its up and left grid, keep a tuple of length n
        """
        @lru_cache(None)
        def dp(index, memo, intro, extro):
            # print(index, memo, intro, extro)
            if index == m*n or (intro == 0 and extro == 0):
                return 0
            up, left = memo[0], memo[-1]
            i, j = divmod(index, n)
            score = dp(index+1, memo[1:] + tuple([0]), intro, extro) 
            if intro > 0:
                diff = 120 + (i>0)*cost[up][1] + (j>0)*cost[left][1]
                score = max(score, diff+dp(index+1, memo[1:]+tuple([1]), intro-1, extro))
            if extro > 0:
                diff = 40 + (i>0)*cost[up][2] + (j>0)*cost[left][2]
                score = max(score, diff+dp(index+1, memo[1:]+tuple([2]), intro, extro-1))
            return score

        i_loss = -30
        e_gain = 20
        cost = [[0,0,0],[0,2*i_loss,i_loss+e_gain],[0, i_loss+e_gain, 2*e_gain]]
        if n > m:
            m, n = n, m
        return dp(0, tuple([0]*n), introvertsCount, extrovertsCount)

S = Solution()
m = 2
n = 3
introvertsCount = 1
extrovertsCount = 2
print(S.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))
m = 3
n = 1
introvertsCount = 2
extrovertsCount = 1
print(S.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))
m = 2
n = 2
introvertsCount = 4
extrovertsCount = 0
print(S.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))

m = 3
n = 3
introvertsCount = 3
extrovertsCount = 1
print(S.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))

m = 3
n =4
introvertsCount = 6
extrovertsCount = 5
print(S.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))
# 输出：
# 880
# 预期结果：
# 890