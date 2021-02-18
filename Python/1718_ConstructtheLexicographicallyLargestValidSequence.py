"""
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20
"""



from typing import List
class Solution_1:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(idx):
            if self.res is not None:
                return
            print(idx, seq)
            if idx == length:
                self.res = seq[:]
                return
            if seq[idx] != 0:
                backtrack(idx + 1)
            for i in range(n, 0, -1):
                if i not in visited:
                    if i == 1 or (idx + i < length and seq[idx + i] == 0):
                        seq[idx] = i
                        if i != 1:
                            seq[idx + i] = i
                        visited.add(i)
                        backtrack(idx + 1)
                        seq[idx] = 0
                        if i != 1:
                            seq[idx + i] = 0
                        visited.remove(i)


        length = 2 * n - 1
        seq = [0] * length
        visited = set()
        self.res = None
        backtrack(0)
        return self.res

# 作者：chenchuxin
# 链接：https://leetcode-cn.com/problems/construct-the-lexicographically-largest-valid-sequence/solution/tan-xin-hui-su-by-chenchuxin-jcy5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:        
        lens = 2 * n - 1
        ans = [0] * lens
        visited = set()

        def dfs(start):
            if len(visited) == n: return ans
            # 当前位置已经填了，那就进行下一个吧
            if ans[start] > 0: return dfs(start + 1)
            # 贪心：数字从大到小填
            for i in range(n, 0, -1):
                if i in visited: continue
                sec = start + i
                if i == 1 or (sec < lens and ans[sec] == 0):
                    visited.add(i)
                    ans[start] = i
                    if i > 1: 
                        ans[sec] = i
                    if dfs(start + 1): 
                        return ans
                    visited.remove(i)
                    ans[start] = 0
                    if i > 1: 
                        ans[sec] = 0
            return None
        return dfs(0)


from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(idx):
            print(idx, seq)
            if idx == length:
                return seq
            if seq[idx] != 0:
                return backtrack(idx + 1)
            for i in range(n, 0, -1):
                if i not in visited:
                    if i == 1 or (idx + i < length and seq[idx + i] == 0):
                        seq[idx] = i
                        if i > 1:
                            seq[idx + i] = i
                        visited.add(i)
                        if backtrack(idx + 1):
                            return seq
                        seq[idx] = 0
                        if i > 1:
                            seq[idx + i] = 0
                        visited.remove(i)
            return None

        length = 2 * n - 1
        seq = [0] * length
        visited = set()
        return backtrack(0)



S = Solution()
print(S.constructDistancedSequence(3))
print(S.constructDistancedSequence(5))
print(S.constructDistancedSequence(2))