"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
Note: The length of each dimension in the given grid does not exceed 50.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-distinct-islands-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numDistinctIslands2(self, grid) -> int:
        """
        use bitmask to represent island, rotate the island 90, 180, 270, union the bitmask sign after rotation to the original bitmask sign
        wrong answer, do not do all the rotation and transformation required in the problem
        旋转和翻转的两种方法：
        模拟岛屿的旋转和翻转有很多种方法，在 Python 代码中，我们把坐标看成复数，每次将坐标乘以单位虚数 1j 就是一次旋转操作。对于翻转操作，将坐标的实部和虚部交换即可。在 Java 代码中，我们直接进行旋转和翻转操作，对于坐标 (x, y)(x,y)，它的 8 种情况分别为 (x, y), (-x, y), (x, -y), (-x, -y), (y, x), (-y, x), (y, -x), (-y, -x)(x,y),(−x,y),(x,−y),(−x,−y),(y,x),(−y,x),(y,−x),(−y,−x)。

        """
        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i, j, res):
            """
            return the right bottom corner of an island
            """
            visited[i][j] = 1
            res[0] = min(i, res[0])
            res[1] = min(j, res[1])
            res[2] = max(i, res[2])
            res[3] = max(j, res[3])
            for di, dj in dir4:
                ni, nj = i+di, j+dj
                if inRange(ni, nj) and visited[ni][nj] == 0 and grid[ni][nj] == 1:
                    dfs(ni, nj, res)

        def mask_matrix(matrix):
            m1 = []
            m2 = []
            for row in matrix:
                str_row = ''.join(str(i) for i in row)
                m1.append(int(str_row, 2))
                m2.append(int(str_row[::-1], 2))
            t1 = tuple(m1)
            t2 = tuple(m1[::-1])
            t3 = tuple(m2)
            t4 = tuple(m2[::-1])
            # print(res, res in shapes)
            return set([t1, t2, t3, t4])

        def island_mask(lst):
            """
            change list of nodes to string
            """
            si,sj,ei,ej = lst
            # print(lst)
            matrix = []
            for i in range(si, ei+1):
                matrix.append(grid[i][sj:ej+1])
            t_matrix = [list(row) for row in zip(*matrix)]
            s1, s2 = mask_matrix(matrix), mask_matrix(t_matrix)
            s = s1 | s2
            node = s.pop()
            for i in s:
                union(i, node)
            return find(node)

        def find(mask):
            if mask not in root:
                root[mask] = mask
            if root[mask] != mask:
                root[mask] = find(root[mask])
            return root[mask]

        def union(w1, w2):
            r1, r2 = find(w1), find(w2)
            if r1 == r2:
                return False
            root[r1] = r2
            return True

        R, C = len(grid), len(grid[0])
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        shapes = set()
        # for row in grid:
        #     print(row)
        visited = [[0]*C for _ in range(R)]
        root = dict()
        for i in range(R):
            for j in range(C):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    lst = [i,j,i,j] # the 4 corner index of of the island
                    dfs(i,j,lst)
                    # print(i,j,lst)
                    shapes.add(island_mask(lst))
        # print(shapes)
        # print(root)
        return len(shapes)


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/number-of-distinct-islands-ii/solution/bu-tong-dao-yu-de-shu-liang-ii-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# from cmath import complex
class Solution:
    def numDistinctIslands2(self, grid):
        def inRange(r, c):
            return 0 <= r < R and 0 <= c < C

        def dfs(r, c):
            if inRange(r, c) and grid[r][c] == 1 and (r, c) not in seen:
                seen.add((r, c))
                shape.add(complex(r, c))
                for di,dj in dir4:
                    dfs(di+r, dj+c)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                # print('shape', shape, sorted(str(z-w) for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = ['']
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans, translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        shapes = set()
        seen = set()
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                shape = set()
                dfs(r, c)
                if shape:
                    shapes.add(canonical(shape))
        print(shapes)
        return len(shapes)


'''
dfs把连通域枚举出来，然后每一个连通域中的节点和连通域的左上角取相对坐标，然后排序后
的点序列作为hash值，8个hash都没有出现过的形状才认为是第一次出现的形状，统计
不同的形状出现次数
'''
# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/number-of-distinct-islands-ii/solution/python-dfs-hash-by-hao-shou-bu-juan/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def numDistinctIslands2(self, grid) -> int:
        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i, j):
            pos.append((i, j))
            visited[i][j] = 1
            for di,dj in dir4:
                ni, nj = i+di, j+dj
                if inRange(ni, nj) and visited[ni][nj] == 0 and grid[ni][nj] == 1:
                    dfs(ni, nj)

        def getHash(pos):
            min_i, min_j = min([p[0] for p in pos]), min([p[1] for p in pos])
            ans = [(i-min_i, j-min_j) for i, j in pos]
            ans.sort()
            return tuple(ans)

        R, C = len(grid), len(grid[0])
        visited = [[0 for _ in range(C)] for _ in range(R)]
        hash_record = set()
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        transfer4 = [(1,1),(1,-1),(-1,-1),(-1,1)]
        res = 0
        for i in range(R):
            for j in range(C):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    pos = []
                    dfs(i, j)
                    # print(pos)
                    hash_code = set()
                    for di, dj in transfer4:
                        hash_code.add(getHash([(i*di, j*dj) for i, j in pos]))
                        hash_code.add(getHash([(j*di, i*dj) for i, j in pos]))
                    if len(hash_record) == 0 or len(hash_code & hash_record) == 0:
                        hash_record|= hash_code
                        res += 1
        # print(hash_record)
        return res


S = Solution()
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(S.numDistinctIslands2(grid))
grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
print(S.numDistinctIslands2(grid))
grid = [[0,1,1,1,0,0,0,1,1,1,1,1,0,1,0],[1,1,0,0,0,1,1,0,0,1,0,0,0,1,1],[0,1,1,1,0,1,1,1,0,1,1,0,0,0,1],[0,0,0,0,0,1,0,0,1,0,0,1,1,1,0],[1,0,1,1,1,0,1,1,0,1,1,1,1,1,0],[1,1,0,0,0,1,0,0,1,0,1,1,1,0,0],[0,1,1,0,0,1,1,1,0,1,0,0,0,1,0],[0,0,0,0,0,0,1,0,1,1,0,0,0,1,0],[1,1,1,0,0,1,1,0,0,0,0,1,0,1,1],[1,1,0,1,0,0,0,1,0,0,0,0,0,0,0]]
print(S.numDistinctIslands2(grid))

grid =[[0,0,1],[0,0,1],[1,1,0]]
print(S.numDistinctIslands2(grid))