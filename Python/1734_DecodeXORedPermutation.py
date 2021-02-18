"""
There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

 

Example 1:

Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
Example 2:

Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]
 

Constraints:

3 <= n < 105
n is odd.
encoded.length == n - 1
"""


from typing import List
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        """
        TLE 54/63
        """
        def test(num):
            idx = 0
            perm[idx] = num
            visited[num] = 1
            for e in encoded:
                nxt_num = num ^ e
                if nxt_num > n or nxt_num == 0 or visited[nxt_num] == 1:
                    return False
                visited[nxt_num] = 1
                idx += 1
                perm[idx] = nxt_num
                num = nxt_num
            return sum(visited) == n

        n = len(encoded) + 1
        for i in range(1, n + 1):
            perm = [0] * n
            visited = [0] * (n + 1)
            if test(i):
                # print(perm)
                # print(visited)
                return perm

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        all_xor = 0
        for i in range(1, n + 1):
            all_xor ^= i
        all_but_first = 0
        for i in range(1, len(encoded), 2):
            all_but_first ^= encoded[i]
        first = all_xor ^ all_but_first
        res = [first]
        for e in encoded:
            res.append(res[-1] ^ e)
        return res


S = Solution()
encoded = [3,1]
print(S.decode(encoded))
encoded = [6,5,4,6]
print(S.decode(encoded))
encoded = [3,12,1,15,5,2,3,7]
print(S.decode(encoded))
# 输出：
# [6,5,9,8,7,2,0,3,4]
# 预期：
# [7,4,8,9,6,3,1,2,5]