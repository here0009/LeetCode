"""
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

 

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
 

Constraints:

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-distance-to-target-color
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from bisect import bisect_left
from collections import defaultdict
class Solution:
    def shortestDistanceColor(self, colors, queries):
        index_dict = defaultdict(list)
        for i,v in enumerate(colors):
            index_dict[v].append(i)
        res = []
        # print(index_dict)
        for i,c in queries:
            if c not in index_dict:
                res.append(-1)
            else:

                lst = index_dict[c]
                j = bisect_left(lst, i)
                diff = float('inf')
                if j < len(lst):
                    diff = min(diff, abs(lst[j] - i))
                if j > 0:
                    diff = min(diff, abs(lst[j-1] -i))
                # print(i, j, diff)
                res.append(diff)
        return res


from bisect import bisect_left
from collections import defaultdict
class Solution:
    def shortestDistanceColor(self, colors, queries):
        index_dict = defaultdict(list)
        for i,v in enumerate(colors):
            index_dict[v].append(i)
        res = []
        # print(index_dict)
        for i,c in queries:
            if c not in index_dict:
                res.append(-1)
            else:
                lst = index_dict[c]
                j = bisect_left(lst, i)
                res.append(min((abs(lst[x] - i) for x in [j, j-1] if 0 <= x < len(lst))))
        return res


from collections import defaultdict
class Solution:
    def shortestDistanceColor(self, colors, queries):
        length = len(colors)
        dp_left = [[float('inf')]*length for _ in range(4)]
        dp_right = [[float('inf')]*length for _ in range(4)]
        dp_left[colors[0]-1][0] = 0
        dp_right[colors[-1]-1][-1] = 0
        for i in range(1, length):
            for j in range(3):
                dp_left[j][i] = dp_left[j][i-1] + 1
            dp_left[colors[i]-1][i] = 0
        for i in range(length-2, -1, -1):
            for j in range(3):
                dp_right[j][i] = dp_right[j][i+1] + 1
            dp_right[colors[i]-1][i] = 0
        # for row in dp_left:
        #     print(row)
        # for row in dp_right:
        #     print(row)
        res = []
        for i, c in queries:
            tmp = min(dp_left[c-1][i], dp_right[c-1][i])
            if tmp == float('inf'):
                res.append(-1)
            else:
                res.append(tmp)
        return res


S = Solution()
colors = [1,1,2,1,3,2,2,3,3]
queries = [[1,3],[2,2],[6,1]]
print(S.shortestDistanceColor(colors, queries))
colors = [1,2]
queries = [[0,3]]

print(S.shortestDistanceColor(colors, queries))
