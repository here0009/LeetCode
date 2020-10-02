"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

 

Example 1:


Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.
 

Note:

The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-celebrity
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    """
    TLE
    """
    def findCelebrity(self, n: int) -> int:
        matrix = [[0]*n for _ in range(n)]
        sum_rows, sum_cols = [0]*n, [0]*n
        for i in range(n):
            for j in range(n):
                matrix[i][j] += knows(i,j)
                sum_rows[i] += matrix[i][j]
                sum_cols[j] += matrix[i][j]
        for i in range(n):
            if sum_rows[i] == 1 and sum_cols[i] == n:
                return i
        return -1


class Solution:
    def findCelebrity(self, n: int) -> int:
        bfs = {0}
        # visited = {0}
        while bfs:
            bfs2 = set()
            for i in bfs:
                visited.add(j)
                for j in range(n):
                    if knows(i,j):
                        bfs2.add(i)
            if bfs == bfs2:
                break
            bfs = bfs2
        if len(bfs) != 1:
            return -1
        j = bfs.pop()
        for i in range(n):
            if i == j:
                continue
            if not knows(i,j) or knows(j,i):
                return False
        return j

class Solution:
    def findCelebrity(self, n: int) -> int:
        bfs = {0}
        visited = {0}
        while bfs:
            bfs2 = set()
            for i in bfs:
                for j in range(n):
                    if j not in visited and knows(i,j):
                        bfs2.add(j)
            if not bfs2:
                break
            bfs = bfs2

        if len(bfs) != 1:
            return -1
        
        j = bfs.pop()
        for i in range(n):
            if i == j:
                continue
            if not knows(i,j) or knows(j,i):
                return -1
        return j



class Solution:
    def findCelebrity(self, n: int) -> int:
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i,j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            root[ri] = rj
            return True

        for i in range(n):
            root[i] = i

        bfs = [0]
        while bfs:
            for i in bfs:
                for j in range(n):
                    if knows(i,j):
                        if union(i,j):
                            bfs2.add(j)
            bfs = bfs2


class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        TLE
        """
        bfs = {0}
        visited = {0}
        celebrity = set()
        while bfs:
            bfs2 = set()
            for i in bfs:
                visited.add(i)
                flag = True # if i do not know any of others, i is a celebrity candidate
                for j in range(n):
                    if j != i and j not in visited and knows(i,j):
                        flag = False
                        bfs2.add(j)
                if flag:
                    celebrity.add(i)
                    break
            if flag:
                break
            bfs = bfs2


        if len(celebrity) != 1:
            return -1
        
        j = celebrity.pop()
        for i in range(n):
            if i == j:
                continue
            if not knows(i,j) or knows(j,i):
                return -1
        return j

        
# https://leetcode-cn.com/problems/find-the-celebrity/solution/shuang-zhi-zhen-zhen-hao-yong-java-by-czwhl123/

class Solution:
    def findCelebrity(self, n: int) -> int:
        left, right = 0, n-1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1
        for i in range(n):
            if i == left:
                continue
            if not knows(i, left) or knows(left, i):
                return -1
        return left