"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

class Solution:
    def maxLength(self, arr) -> int:
        """
        use a table to record if two subseq got the overlap letters, then dfs to find the res
        WRONG IDEA
        """
        n = len(arr)
        table = [[1]*n for _ in range(n)]
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            table[i][i] = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if len(set(arr[i]) & set(arr[j])) > 0: #got overlap
                    table[i][j] = 0
                    table[j][i] = 0

        for row in table:
            print(row)
        self.res = 0
        def dfs(i, length):
            self.res = max(self.res, length)
            for j in range(n):
                if not visited[i][j] and table[i][j] == 1:
                    visited[i][j] = 1
                    dfs(j, length+len(arr[j]))
                    visited[i][j] = 0

        for i in range(n):
            dfs(i, len(arr[i]))

        return self.res


class Solution:
    def maxLength(self, arr) -> int:
        """
        """
        n = len(arr)
        res = [set()]
        for s in arr:
            set_s = set(s)
            if len(s) > len(set_s):
                continue

            for set_r in res:
                if len(set_s & set_r) == 0:
                    res.append(set_s | set_r)
        # print(res)
        return max(len(s) for s in res)

s = Solution()
arr = ["un","iq","ue"]
print(s.maxLength(arr))

arr = ["cha","r","act","ers"]
print(s.maxLength(arr))

arr = ["abcdefghijklmnopqrstuvwxyz"]
print(s.maxLength(arr))


arr = ["yy","bkhwmpbiisbldzknpm"]
print(s.maxLength(arr))