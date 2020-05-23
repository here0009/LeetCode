"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""
class Solution_1:
    def findCircleNum(self, M) -> int:
        def dfs(i,color):
            if visited[i] == 0:
                visited[i] = color
                for j in range(len(M[i])):
                    if M[i][j] == 1:
                        dfs(j,color)
            return


        visited = [0]*len(M)
        color = 0
        for i in range(len(M)):
            if visited[i] == 0:
                color +=1
                dfs(i,color)
        return color

class Solution_2:
    def findCircleNum(self, M) -> int:
        def find(node):
            if circles[node] == node:
                return node
            root = find(node)
            circles[node] = root
            return root

        n = len(M)
        circles = {x:x for x in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j] == 1 and find(i) != find(j):
                    circles[find(i)] = find(j)
        # print(circles)
        return sum([1 for k,v in circles.items() if k==v])


class Solution:
    def findCircleNum(self, M) -> int:
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x,y):
            if find(x) != find(y):
                parents[find(x)] = find(y)

        len_M = len(M)
        parents = {x:x for x in range(len_M)}
        for i in range(len_M):
            for j in range(i+1,len_M):
                if M[i][j] == 1:
                    union(i,j)

        res = set(find(k) for k in parents)
        return len(res)



s = Solution()
# M = [[1,1,0],[1,1,0],[0,0,1]]
# print(s.findCircleNum(M))

# M = [[1,1,0],[1,1,1],[0,1,1]]
# print(s.findCircleNum(M))

# M = [[1]]
# print(s.findCircleNum(M))

# M = [[0]]
# print(s.findCircleNum(M))

M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(s.findCircleNum(M))