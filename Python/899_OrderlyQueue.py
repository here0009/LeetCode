"""
A string S of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first K letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.

 

Example 1:

Input: S = "cba", K = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".

Example 2:

Input: S = "baaca", K = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".
 

Note:

1 <= K <= S.length <= 1000
S consists of lowercase letters only.
"""



class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        """
        maximum recursion depth exceeded in comparison
        """
        def dfs(string):
            if string < self.res:
                self.res = string
            for i in range(K):
                s2 = string[:i] + string[i + 1:] + string[i]
                if s2 not in visited:
                    visited.add(s2)
                    dfs(s2)

        self.res = S
        visited = set([S])
        dfs(S)
        return self.res


class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        """
        Thoughts: 
        because there is no swap limitation, if K >= 2, we can swap any two letters
        if K == 1, there's only len(S) options (S[:i] + S[i:] for i in range(len(S)))
        """
        return ''.join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))


Slt = Solution()
S = "cba"
K = 1
print(Slt.orderlyQueue(S, K))
S = "baaca"
K = 3
print(Slt.orderlyQueue(S, K))
S = "mqvgtdfuiv"
K = 10
print(Slt.orderlyQueue(S, K))