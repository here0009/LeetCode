"""
There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
 

Example 1:

Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]
 

Example 2:

Input: n = 2, m = 1.
Output: 3
Explanation: Status can be: [on, off], [off, on], [off, off]
 

Example 3:

Input: n = 3, m = 1.
Output: 4
Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
 

Note: n and m both fit in range [0, 1000].
"""


from collections import defaultdict
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        def dfs(status, k):
            # print(bin(status), k)
            if k == m:
                return
            for i in nums:
                s2 = status ^ i
                if s2 not in visited[k + 1]:
                    visited[k + 1].add(s2)
                    dfs(s2, k + 1)

        a, b, c, d = '', '', '', ''
        for i in range(n):  # shift 1~n to 0~n-1
            a += '1'
            if i % 2 == 0:
                c += '1'
                b += '0'
            else:
                c += '0'
                b += '1'
            if i % 3 == 0:
                d += '1'
            else:
                d += '0'
        nums = set()
        for i in [a, b, c, d]:
            nums.add(int(i, 2))
        # print(nums)
        visited = defaultdict(set)
        visited[0].add(0)
        dfs(0, 0)
        # print(visited)
        return len(visited[m])

# for i in range(40):
#     print(i, 3*i+1)
S = Solution()
n = 1
m = 1
print(S.flipLights(n, m))
n = 2
m = 1
print(S.flipLights(n, m))
n = 3
m = 1
print(S.flipLights(n, m))
n = 2
m = 2
print(S.flipLights(n, m))
# Output
# 3
# Expected
# 4