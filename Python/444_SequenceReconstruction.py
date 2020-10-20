"""
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

 

Example 1:

Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true
 

Constraints:

1 <= n <= 10^4
org is a permutation of {1,2,...,n}.
1 <= segs[i].length <= 10^5
seqs[i][j] fits in a 32-bit signed integer.
 

UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sequence-reconstruction
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
from collections import Counter
class Solution:
    def sequenceReconstruction(self, org, seqs) -> bool:
        """
        topological sort
        """
        edges = defaultdict(list)
        indegree = Counter()
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
            for i in range(1, len(seq)):
                p, q = seq[i-1], seq[i]
                edges[p].append(q)
                indegree[q] += 1
        res = []
        nodes -= set(indegree.keys())
        while nodes:
            if len(nodes) > 1:
                return False
            node = nodes.pop()
            res.append(node)
            for next_node in edges[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    nodes.add(next_node)
        return org == res and all(k == 0 for k in indegree.values())


S = Solution()
org = [1,2,3]
seqs = [[1,2],[1,3]]
print(S.sequenceReconstruction(org, seqs))
org = [1,2,3]
seqs = [[1,2]]
print(S.sequenceReconstruction(org, seqs))
org = [1,2,3]
seqs = [[1,2],[1,3],[2,3]]
print(S.sequenceReconstruction(org, seqs))
org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]
print(S.sequenceReconstruction(org, seqs))
org = [1]
seqs = [[1],[1],[1]]
print(S.sequenceReconstruction(org, seqs))
# 输出：
# false
# 预期结果：
# true
org = [1,2,3,4,5]
seqs = [[1,2,3,4,5],[1,2,3,4],[1,2,3],[1],[4],[5]]
print(S.sequenceReconstruction(org, seqs))
# 输出：
# false
# 预期结果：
# true
org = [1]
seqs = [[1],[2,3],[3,2]]
print(S.sequenceReconstruction(org, seqs))