"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        res = 0
        # for i in range(n)
        distance_matrix = [[0]*n for i in range(n)]
        # print(distance_matrix)
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = self.squared_distance(points[i], points[j])
        # print(distance_matrix)
        for i in range(n):
            tmp_dict = dict()
            for j in range(n):
                tmp_dict[distance_matrix[i][j]] = tmp_dict.get(distance_matrix[i][j], 0) + 1
            for value in tmp_dict.values():
                res += value * (value -1)
        return res

    def squared_distance(self, p1, p2):
        '''
        return the square distance between p1 and p2
        '''
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

class Solution_2:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        
        for x1, y1 in points:
            cnts = {}
            
            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                d = dx * dx + dy * dy
                
                if d in cnts:
                    ans += cnts[d] #一个点之后, 每增加一个点, 这个点与原有的点可以形成cnts[d]对组合
                    cnts[d] += 1
                else:
                    cnts[d] = 1
        
        return 2 * ans



points = [[0,0],[1,0],[2,0]]
s = Solution()
print(s.numberOfBoomerangs(points))