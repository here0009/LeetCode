"""
You are given an integer n and an integer p representing an array arr of length n where all elements are set to 0's, except position p which is set to 1. You are also given an integer array banned containing restricted positions. Perform the following operation on arr:

Reverse a subarray with size k if the single 1 is not set to a position in banned.
Return an integer array answer with n results where the ith result is the minimum number of operations needed to bring the single 1 to position i in arr, or -1 if it is impossible.



Example 1:

Input: n = 4, p = 0, banned = [1,2], k = 4

Output: [0,-1,-1,1]

Explanation:

Initially 1 is placed at position 0 so the number of operations we need for position 0 is 0.
We can never place 1 on the banned positions, so the answer for positions 1 and 2 is -1.
Perform the operation of size 4 to reverse the whole array.
After a single operation 1 is at position 3 so the answer for position 3 is 1.
Example 2:

Input: n = 5, p = 0, banned = [2,4], k = 3

Output: [0,-1,-1,-1,-1]

Explanation:

Initially 1 is placed at position 0 so the number of operations we need for position 0 is 0.
We cannot perform the operation on the subarray positions [0, 2] because position 2 is in banned.
Because 1 cannot be set at position 2, it is impossible to set 1 at other positions in more operations.
Example 3:

Input: n = 4, p = 2, banned = [0,1,3], k = 1

Output: [-1,-1,0,-1]

Explanation:

Perform operations of size 1 and 1 never changes its position.



Constraints:

1 <= n <= 105
0 <= p <= n - 1
0 <= banned.length <= n - 1
0 <= banned[i] <= n - 1
1 <= k <= n
banned[i] != p
all values in banned are unique
"""
from typing import List


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        # print('='*30)
        res = [-1]*n
        banned_set = set(banned)
        # print(banned_set)
        res[p] = 0
        if k <= 1:
            return res
        step = 0
        visited = [0]*n
        bfs = [p]
        while bfs:
            # print(bfs)
            bfs2 = []
            for node in bfs:
                res[node] = step
                visited[node] = 1
                for next_node in [(node + k - 1) % n, (node - k + 1) % n]:
                    if visited[next_node] == 0 and next_node not in banned_set:
                        bfs2.append(next_node)
            step += 1
            bfs = list(set(bfs2))
        return res

S = Solution()
n = 4
p = 0
banned = [1,2]
k = 4
print(S.minReverseOperations(n, p, banned, k))
n = 5
p = 0
banned = [2,4]
k = 3
print(S.minReverseOperations(n, p, banned, k))
n = 4
p = 2
banned = [0,1,3]
k = 1
print(S.minReverseOperations(n, p, banned, k))
n = 2
p = 1
banned = []
k = 2
print(S.minReverseOperations(n, p, banned, k))