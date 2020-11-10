"""
Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7

 

Example 1:

Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.
Example 2:

Input: instructions = [1,2,3,6,5,4]
Output: 3
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
Example 3:

Input: instructions = [1,3,3,3,2,4,2,1,2]
Output: 4
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.
 

Constraints:

1 <= instructions.length <= 105
1 <= instructions[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/create-sorted-array-through-instructions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from bisect import insort, bisect_left, bisect_right
from typing import List
class Solution:
    def createSortedArray(self, instructions) -> int:
        M = 10**9 + 7
        lst = []
        res = 0
        for i,v in enumerate(instructions):
            left = bisect_left(lst, v)
            right = bisect_right(lst, v)
            res += min(left, i - right)
            insort(lst, v)
        return res % M


from bisect import insort, bisect_left, bisect_right
class Solution:
    def createSortedArray(self, instructions) -> int:
        M = 10**9 + 7
        lst = []
        res = 0
        for i,v in enumerate(instructions):
            left = bisect_left(lst, v)
            right = bisect_right(lst, v)
            res += min(left, i - right)
            lst[left:left] = [v]
        return res % M


from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, ins):
        ans = 0
        cc = SortedList()
        MOD = 1000000007
        for n in ins:
            cost = min(cc.bisect_left(n), len(cc) - cc.bisect_right(n))
            ans = (ans + cost) % MOD
            cc.add(n)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        N = max(instructions)
        cc = [0] * (N + 1)

        def update(x):
            while x <= N:
                cc[x] += 1
                x += -x & x

        def query(x):
            ans = 0
            while x > 0:
                ans += cc[x]
                x -= -x & x
            return ans

        ans = 0
        for i, n in enumerate(instructions):
            ans += min(query(n - 1), i - query(n))
            update(n)
        return ans % MOD
# https://leetcode.com/problems/create-sorted-array-through-instructions/discuss/927531/JavaC%2B%2BPython-Binary-Indexed-Tree
class Solution:
    def createSortedArray(self, A) -> int:
        def update(x):
            print('update',x)
            while (x <= m):
                print(x)
                c[x] += 1
                x += x & -x

        def get(x):
            print('get x',x)
            res = 0
            while (x > 0):
                print(x)
                res += c[x]
                x -= x & -x
            print('res',res)
            return res

        res = 0
        m = max(A)
        c = [0] * (m + 1)
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
            print(i,a,bin(a), c, res)
        return res % (10**9 + 7)

# https://leetcode-cn.com/problems/create-sorted-array-through-instructions/comments/
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10 ** 9 + 7
        bit = BIT(max(instructions))
        res = 0
        for i, x in enumerate(instructions):
            left = bit.query(x - 1)
            right = i - bit.query(x)
            res += min(left, right)
            res %= mod
            bit.update(x, 1)
        return res

class BIT:
    def __init__(self, n):
        self.n = n
        self.d = [0] * (n + 1)
    
    def update(self, x, v):
        while x <= self.n:
            self.d[x] += v
            x += self.lowbit(x)
    
    def query(self, x):
        res = 0
        while x > 0:
            res += self.d[x]
            x -= self.lowbit(x)
        return res
    
    def lowbit(self, x):
        return x & (-x)

class Solution:
    def createSortedArray(self, A) -> int:
        def get(i):
            """
            retutn counts of nums <= i
            """
            res = counts[i]
            while i > 0:
                i -= i & -i
                res += counts[i]
            return res
        def insert(i):
            """
            insert i to fenwick tree
            """
            while i <= length:
                counts[i] += 1
                i += i & -i


        length = max(A)
        M = 10**9+7
        counts = [0]*(length+1)
        res = 0
        for i, v in enumerate(A):
            res = (res + min(get(v-1), i-get(v))) % M
            insert(v)
        return res


S = Solution()
instructions = [1,5,6,2]
print(S.createSortedArray(instructions))
instructions = [1,2,3,6,5,4]
print(S.createSortedArray(instructions))
instructions = [1,3,3,3,2,4,2,1,2]
print(S.createSortedArray(instructions))
