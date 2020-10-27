"""
Your task is to design the basic function of Excel and implement the function of sum formula. Specifically, you need to implement the following functions:

Excel(int H, char W): This is the constructor. The inputs represents the height and width of the Excel form. H is a positive integer, range from 1 to 26. It represents the height. W is a character range from 'A' to 'Z'. It represents that the width is the number of characters from 'A' to W. The Excel form content is represented by a height * width 2D integer array C, it should be initialized to zero. You should assume that the first row of C starts from 1, and the first column of C starts from 'A'.


void Set(int row, char column, int val): Change the value at C(row, column) to be val.


int Get(int row, char column): Return the value at C(row, column).


int Sum(int row, char column, List of Strings : numbers): This function calculate and set the value at C(row, column), where the value should be the sum of cells represented by numbers. This function return the sum result at C(row, column). This sum formula should exist until this cell is overlapped by another value or another sum formula.

numbers is a list of strings that each string represent a cell or a range of cells. If the string represent a single cell, then it has the following format : ColRow. For example, "F7" represents the cell at (7, F).

If the string represent a range of cells, then it has the following format : ColRow1:ColRow2. The range will always be a rectangle, and ColRow1 represent the position of the top-left cell, and ColRow2 represents the position of the bottom-right cell.


Example 1:
Excel(3,"C"); 
// construct a 3*3 2D array with all zero.
//   A B C
// 1 0 0 0
// 2 0 0 0
// 3 0 0 0

Set(1, "A", 2);
// set C(1,"A") to be 2.
//   A B C
// 1 2 0 0
// 2 0 0 0
// 3 0 0 0

Sum(3, "C", ["A1", "A1:B2"]);
// set C(3,"C") to be the sum of value at C(1,"A") and the values sum of the rectangle range whose top-left cell is C(1,"A") and bottom-right cell is C(2,"B"). Return 4. 
//   A B C
// 1 2 0 0
// 2 0 0 0
// 3 0 0 4

Set(2, "B", 2);
// set C(2,"B") to be 2. Note C(3, "C") should also be changed.
//   A B C
// 1 2 0 0
// 2 0 2 0
// 3 0 0 6
Note:
You could assume that there won't be any circular sum reference. For example, A1 = sum(B1) and B1 = sum(A1).
The test cases are using double-quotes to represent a character.
Please remember to RESET your class variables declared in class Excel, as static/class variables are persisted across multiple test cases. Please see here for more details.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-excel-sum-formula
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
from collections import Counter
class Excel:
    """
    wrong answer
    """
    def intcol(self, W):
        return ord(W) - ord('A')

    def strToindex(self, string):
        return int(string[1:]), self.intcol(string[0])

    def __init__(self, H: int, W: str):
        self.matrix = [[0]*(self.intcol(W) + 1) for _ in range(H+1)]
        self.edges_to = defaultdict(Counter)
        self.edges_from = defaultdict(Counter)

    def set(self, r: int, c: str, v: int) -> None:
        ic = self.intcol(c)
        pre_v = self.get(r, c)
        self.matrix[r][ic] = v
        for key, val in self.edges_to[(r, ic)].items():
            i, j = key
            self.matrix[i][j] += (v - pre_v)*val
        for i,j in self.edges_from[(r,ic)]:
            del self.edges_to[(i,j)][(r,ic)]
        for row in self.matrix:
            print(row)

    def get(self, r: int, c: str) -> int:
        return self.matrix[r][self.intcol(c)]

    def sum(self, r: int, c: str, strs) -> int:
        res = 0
        ic = self.intcol(c)
        for string in strs:
            if ':' not in string:
                i,j = self.strToindex(string)
                res += self.matrix[i][j]
                self.edges_to[(i,j)][(r,ic)] += 1
                self.edges_from[(r, ic)][(i,j)] += 1
            else:
                start, end = string.split(':')
                i_start, j_start = self.strToindex(start)
                i_end, j_end = self.strToindex(end)
                for i in range(i_start, i_end+1):
                    for j in range(j_start, j_end+1):
                        res += self.matrix[i][j]
                        self.edges_to[(i,j)][(r,ic)] += 1
                        self.edges_from[(r, ic)][(i,j)] += 1
        self.matrix[r][ic] = res
        return res


# Your Excel object will be instantiated and called as such:
obj = Excel(3,"C")
print(obj.set(1, "A", 2))
print(obj.sum(3, "C", ["A1", "A1:B2"]))
print(obj.set(2, "B", 2))

# 输入：
# ["Excel","set","sum","set","get","set","get"]
# [[5,"E"],[1,"A",1],[2,"B",["A1"]],[2,"B",0],[2,"B"],[1,"A",5],[2,"B"]]
# 输出：
# [null,null,1,null,0,null,4]
# 预期结果：
# [null,null,1,null,0,null,0]

# ["Excel","get","set","get","sum","set","get"]
# [[5,"E"],[1,"A"],[1,"A",1],[1,"A"],[2,"B",["A1","A1"]],[1,"A",2],[2,"B"]]

# 输出：
# [null,0,null,1,2,null,3]
# 预期结果：
# [null,0,null,1,2,null,4]

# ["Excel","set","set","set","sum","get","set","get","sum","set","get","get","sum","set","get","get","get","get"]
# [[5,"E"],[1,"A",5],[1,"B",3],[1,"C",2],[1,"C",["A1","A1:B1"]],[1,"C"],[1,"B",5],[1,"C"],[1,"B",["A1:A5"]],[5,"A",10],[1,"B"],[1,"C"],[3,"C",["A1:C1","A1:A5"]],[3,"A",3],[1,"B"],[1,"C"],[3,"C"],[5,"A"]]

# 输出：
# [null,null,null,null,13,13,null,15,5,null,15,15,50,null,18,15,53,10]
# 预期结果：
# [null,null,null,null,13,13,null,15,5,null,15,25,60,null,18,28,69,10]


# 作者：ming-ye
# 链接：https://leetcode-cn.com/problems/design-excel-sum-formula/solution/xi-jie-chao-duo-de-yi-ti-by-ming-ye/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Cell:
    def __init__(self,val=0,dic={}):
        self.val = val
        self.dic = dic

class Excel:

    def __init__(self, H: int, W: str):
        self.rows = H
        self.cols = ord(W) - ord('A') + 1
        self.cells = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]

    def set(self, r: int, c: str, v: int) -> None:
        row = r - 1
        col = ord(c) - ord('A')

        self.cells[row][col] = Cell(val=v)

        key = c+str(r)
        relation_stack = []
        self.get_relation_cell(key,relation_stack)
        self.cacl_stack(relation_stack)

    def cacl_stack(self,stack):
        stack.pop()

        while stack:
            r,c = stack.pop()
            sum_val = 0
 
            for k,v in self.cells[r][c].dic.items():
                col = ord(k[0]) - ord('A')
                row = int(k[1:]) - 1
                sum_val += self.cells[row][col].val * v
            self.cells[r][c].val = sum_val
        
    def get_relation_cell(self,key,stack):
        for r in range(self.rows):
            for c in range(self.cols):
                if key in self.cells[r][c].dic:
                    self.get_relation_cell(str(chr(c+ord('A')))+str(r+1),stack)
        col = ord(key[0]) - ord('A')
        row = int(key[1:]) - 1
        stack.append([row,col])

    def get(self, r: int, c: str) -> int:
        row = r - 1
        col = ord(c) - ord('A')
        return self.cells[row][col].val

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        all_cells = {}
        sum_val = 0
        for s in strs:
            if ':' in s:
                cells = s.split(':')
                start_c,end_c = cells[0],cells[1]
                s_col = ord(start_c[0]) - ord('A')
                s_row = int(start_c[1:]) - 1
                e_col = ord(end_c[0]) - ord('A')
                e_row = int(end_c[1:]) - 1
                for r1 in range(s_row,e_row+1):
                    for c1 in range(s_col,e_col+1):
                        sum_val += self.cells[r1][c1].val
                        #此处犯了个错，把int值转成ASCII码的时候没有加上’A‘的ASCII码
                        key = chr(c1+ord('A'))+str(r1+1)
                        if key not in all_cells:
                            all_cells[key] = 0
                        all_cells[key] += 1
            else:
                col = ord(s[0]) - ord('A')
                row = int(s[1:]) - 1
                sum_val += self.cells[row][col].val
                if s not in all_cells:
                    all_cells[s] = 0
                all_cells[s] += 1
        
        self.set(r,c,sum_val)
        self.cells[r-1][ord(c) - ord('A')].dic = all_cells
        return sum_val
                

# 作者：kakurin
# 链接：https://leetcode-cn.com/problems/design-excel-sum-formula/solution/python3-by-kakurin/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Excel:
    def __init__(self, H: int, W: str):
        self.w = self.char_to_num(W)
        self.h = H
        self.nums = [[0]*(self.w+1) for _ in range (self.h+1)]
        for i in range (1, self.h+1):
            self.nums[i][0] = i
        for i in range (1, self.w+1):
            self.nums[0][i] = chr(ord('A')+i-1)

        self.prev_sum = {}

    def char_to_num(self, c):
        return ord(c)-ord('A')+1

    def in_strs(self, s, strs):
        count = 0
        for string in strs:
            if string.find(':') == -1:
                if s == string:
                    count += 1
            else:
                idx = string.find(':')+1
                if string[:1]<=s[:1]<=string[idx:idx+1] and int(string[1:idx-1])<=int(s[1:])<=int(string[idx+1:]):
                    count += 1
        return count

    def set(self, r: int, c: str, v: int) -> None:
        v_old = self.get(r, c)
        self.nums[r][self.char_to_num(c)] = v

        curr = c+str(r)
        if curr in self.prev_sum:
            del self.prev_sum[curr]

        if len(self.prev_sum) > 0:
            candidate = []
            while curr:
                for key in self.prev_sum:
                    if curr == key:
                        continue
                    prev = self.prev_sum[key]
                    ct = self.in_strs(curr, prev)
                    if ct > 0:
                        self.nums[int(key[1:])][self.char_to_num(key[0])] += ct*(v-v_old)
                        candidate.append(key)

                curr = None if not candidate else candidate.pop(-1)

    def get(self, r: int, c: str) -> int:
        return self.nums[r][self.char_to_num(c)]

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        self.prev_sum[c+str(r)] = [x for x in strs]

        sums = 0
        while strs:
            s = strs.pop(0)
            
            if s.find(':') == -1:
                sums += self.nums[int(s[1:])][self.char_to_num(s[:1])]
            else:
                idx = s.find(':')+1
                h_start = int(s[1:idx-1])
                h_end = int(s[idx+1:])

                w_start = self.char_to_num(s[:1])
                w_end = self.char_to_num(s[idx])

                for i in range (h_start, h_end+1):
                    for j in range (w_start, w_end+1):
                        sums += self.nums[i][j]

        self.nums[r][self.char_to_num(c)] = sums
        return sums



'''
维护矩阵中每一行中每一个位置的前缀和，
更新数值时候只更新前缀和，计算区域总和时候用每一行的前缀和辅助求和
用hash表维护每一个sum调用后新增的目标位置和计算该位置数值的区域之间的映射关系
'''
# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/design-excel-sum-formula/solution/python-qian-zhui-he-ying-yong-by-hao-shou-bu-juan/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 
from typing import List
class Excel:

    def __init__(self, H: int, W: str):
        self.m = H
        self.n = ord(W) - ord('A') + 1
        self.prefix_sum = [[0 for _ in range(self.n)] for _ in range(self.m)]       # 每一行的前缀和

        self.area_list = {}
        self.target2rules = {}


    def set(self, r: int, c: str, v: int) -> None:
        r = r-1
        c = ord(c) - ord('A')

        if (r, c) in self.target2rules:
            self.target2rules.pop((r, c))

        self._set(r, c, v)

    def _set(self, r: int, c: int, v: int):

        orig_val = self.prefix_sum[r][0] if c == 0 else self.prefix_sum[r][c] - self.prefix_sum[r][c - 1]
        sub = v - orig_val
        if sub == 0:
            return

        for j in range(c, self.n):
            self.prefix_sum[r][j] += sub

        for (target_i, target_j), rules in self.target2rules.items():
            flag = False
            for min_i, max_i, min_j, max_j in set(rules):
                if r >= min_i and r <= max_i and c >= min_j and c <= max_j:
                    flag = True
                    ans = 0
                    for i in range(min_i, max_i + 1):
                        val = self.prefix_sum[i][max_j] if min_j == 0 else self.prefix_sum[i][max_j] - self.prefix_sum[i][min_j - 1]
                        ans += val
                    self.area_list[(min_i, max_i, min_j, max_j)] = ans

            if flag:
                sum_val = 0
                for min_i, max_i, min_j, max_j in rules:
                    sum_val += self.area_list[(min_i, max_i, min_j, max_j)]
                self._set(target_i, target_j, sum_val)

    def get(self, r: int, c: str) -> int:
        r = r-1
        c = ord(c) - ord('A')
        if r > self.m or c > self.n or r < 0 or c < 0:
            return -1
        return self.prefix_sum[r][0] if c == 0 else self.prefix_sum[r][c] - self.prefix_sum[r][c-1]

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        r = r-1
        c = ord(c) - ord('A')

        self.target2rules[(r, c)] = []
        for s in strs:
            parts = s.split(':')
            if len(parts) == 1:
                col = ord(s[0]) - ord('A')
                row = int(s[1:]) - 1

                if (row, row, col, col) not in self.area_list:
                    self.area_list[(row, row, col, col)] = 0

                self.target2rules[(r, c)].append((row, row, col, col))

            else:
                col1 = ord(parts[0][0]) - ord('A')
                row1 = int(parts[0][1:]) - 1
                col2 = ord(parts[1][0]) - ord('A')
                row2 = int(parts[1][1:]) - 1

                area = (min(row1, row2), max(row1, row2), min(col1, col2), max(col1, col2))
                if area not in self.area_list:
                    self.area_list[area] = 0

                self.target2rules[(r, c)].append(area)


        sum_val = 0
        for min_i, max_i, min_j, max_j in self.target2rules[(r, c)]:
            ans = 0
            for i in range(min_i, max_i+1):
                val = self.prefix_sum[i][max_j] if min_j == 0 else self.prefix_sum[i][max_j] - self.prefix_sum[i][min_j - 1]
                ans += val
            self.area_list[(min_i, max_i, min_j, max_j)] = ans
            sum_val += ans

        self._set(r, c, sum_val)

        sum_val = 0
        for min_i, max_i, min_j, max_j in self.target2rules[(r, c)]:
            ans = 0
            for i in range(min_i, max_i + 1):
                val = self.prefix_sum[i][max_j] if min_j == 0 else self.prefix_sum[i][max_j] - self.prefix_sum[i][min_j - 1]
                ans += val
            sum_val += ans
        return sum_val

# 1. 对于sum(self, r: int, c: str, strs)， 将strs中的节点视为节点(r,c)的子节点。
# 2. 使用Cell储存每个节点，cell包括两个属性，val及edges。edges储存其子节点坐标及个数。
# 3. 对于数值类型的节点，get返回其val。对于链接类型的几点，get返回其所有子节点的和。
# from collections import Counter
class Cell:
    def __repr__(self):
        res = ''
        for k, v in self.edges.items():
            res += '(({},{}):{})'.format(k[0],k[1], v)
        return str(self.val) + res

    def __init__(self, val):
        self.val = val
        self.edges = Counter()

class Excel:

    def __init__(self, H: int, W: str):
        self.matrix = []
        w = ord(W) - ord('A') + 1
        for i in range(H):
            self.matrix.append([Cell(0) for _ in range(w)])

    def dfs(self, i,j):
        cell = self.matrix[i][j]
        if len(cell.edges) == 0:
            return cell.val
        res = 0
        for k, v in cell.edges.items():
            ni, nj = k
            res += self.dfs(ni, nj) * v
        return res

    def getIndex(self, r, c):
        return r-1, ord(c)-ord('A')

    def strToindex(self, string):
        return int(string[1:])-1, ord(string[0])-ord('A')

    def set(self, r: int, c: str, v: int) -> None:
        i, j = self.getIndex(r, c)
        self.matrix[i][j].val = v
        self.matrix[i][j].edges = Counter()
        # print('+++++++++++')
        # for row in self.matrix:
        #     print(row)

    def get(self, r: int, c: str) -> int:
        i, j = self.getIndex(r, c)
        return self.dfs(i, j)

    def sum(self, r: int, c: str, strs) -> int:
        i, j = self.getIndex(r, c)
        cell = self.matrix[i][j]
        cell.val = 0
        cell.edges = Counter()
        for string in strs:
            if ':' not in string:
                ni, nj = self.strToindex(string)
                cell.edges[(ni, nj)] += 1
            else:
                start, end = string.split(':')
                i_start, j_start = self.strToindex(start)
                i_end, j_end = self.strToindex(end)
                for ni in range(i_start, i_end+1):
                    for nj in range(j_start, j_end+1):
                        cell.edges[(ni,nj)] += 1
        # print('+++++++++++')
        # for row in self.matrix:
        #     print(row)
        return self.dfs(i, j)



# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)

