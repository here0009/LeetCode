"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

Return the minimum possible value of D.length.

 

Example 1:

Input: ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
Example 2:

Input: ["xc","yb","za"]
Output: 0
Explanation: 
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: 
We have to delete every column.
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
"""
class Solution:
    def minDeletionSize(self, A) -> int:
        """
        Thoughts: find the 1st sorted column in A, delete all the columns before it, so return the index of the 1st sorted column.
        But there are equals ones, so the method did not work
        """
        m = len(A)
        n = len(A[0])
        for j in range(n):
            for i in range(1,m):
                if A[i-1][j:] > A[i][j:]:
                    break
                else:
                    return j
        return n

class Solution:
    def minDeletionSize(self, A) -> int:
        def dfs(row_s, row_e, col):
            # print(row_s, row_e, col)
            if col >= n or deleted[col] == 1:
                return

            pre = A[row_s][col]
            equal_flag = False
            equal_s = row_s
            for i in range(row_s+1, row_e):
                # print(pre,A[i][col])
                if A[i][col] < pre:
                    deleted[col] = 1
                    # print(A[i][col] , A[i-1][col])
                    dfs(row_s, row_e,col+1)
                    return
                elif A[i][col] == pre:
                    if not equal_flag:
                        equal_s = i-1
                        equal_flag = True
                else:
                    if equal_flag:
                        dfs(equal_s, i, col+1)
                        equal_flag = False
                pre = A[i][col]

            if equal_flag:
                dfs(equal_s, row_e, col+1)
                equal_flag = False
                # equal_s = i

        m = len(A)
        n = len(A[0])
        deleted = [0]*n
        dfs(0,m,0)

        return sum(deleted)

class Solution:
    def minDeletionSize(self, A) -> int:
        """
        use a set to keep the sorted rows
        """
        m,n = len(A),len(A[0])
        unsorted = {i for i in range(m-1)}
        res = 0
        for j in range(n):
            if any(A[i][j] > A[i+1][j] for i in unsorted):
                res += 1
            else:
                unsorted -= {i for i in unsorted if A[i][j] < A[i+1][j]}
        return res

class Solution:
    def minDeletionSize(self, A) -> int:
        """
        use a list to keep the sorted rows
        """
        m,n = len(A),len(A[0])
        is_sorted = [0]*m
        res = 0
        for j in range(n):
            is_sorted2 = is_sorted[:]
            for i in range(m-1):
                if A[i][j] > A[i+1][j] and is_sorted[i] == 0: #the row is not sorted befor, and there is an unordered row
                    res += 1
                    break
                elif A[i][j] < A[i+1][j]:
                    is_sorted2[i] = 1
            else:
                is_sorted = is_sorted2 #if there is a break, so the row is not sorted, do not update it
        return res


class Solution:
    def minDeletionSize(self, A) -> int:
        

s = Solution()
A = ["ca","bb","ac"]
print(s.minDeletionSize(A))

A = ["xc","yb","za"]
print(s.minDeletionSize(A))

A = ["zyx","wvu","tsr"]
print(s.minDeletionSize(A))

A = ["xga","xfb","yfa"]
print(s.minDeletionSize(A))

A = ["doeeqiy","yabhbqe","twckqte"]
print(s.minDeletionSize(A))

A = ["abx","agz","bgc","bfc"]
print(s.minDeletionSize(A))
"""
Output
0
Expected
1
"""


A = ["bwwdyeyfhc","bchpphbtkh","hmpudwfkpw","lqeoyqkqwe","riobghmpaa","stbheblgao","snlaewujlc","tqlzolljas","twdkexzvfx","wacnnhjdis"]
print(s.minDeletionSize(A))
# Output
# 2
# Expected
# 4