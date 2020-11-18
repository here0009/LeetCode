"""
You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:

The ith customer gets exactly quantity[i] integers,
The integers the ith customer gets are all equal, and
Every customer is satisfied.
Return true if it is possible to distribute nums according to the above conditions.

 

Example 1:

Input: nums = [1,2,3,4], quantity = [2]
Output: false
Explanation: The 0th customer cannot be given two different integers.
Example 2:

Input: nums = [1,2,3,3], quantity = [2]
Output: true
Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
Example 3:

Input: nums = [1,1,2,2], quantity = [2,2]
Output: true
Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].
Example 4:

Input: nums = [1,1,2,3], quantity = [2,2]
Output: false
Explanation: Although the 0th customer could be given [1,1], the 1st customer cannot be satisfied.
Example 5:

Input: nums = [1,1,1,1,1], quantity = [2,3]
Output: true
Explanation: The 0th customer is given [1,1], and the 1st customer is given [1,1,1].
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= 1000
m == quantity.length
1 <= m <= 10
1 <= quantity[i] <= 105
There are at most 50 unique values in nums.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-repeating-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import Counter
from bisect import bisect_left, insort
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        quantity.sort()
        counts = Counter(nums)
        counts_dict = Counter(counts.values())
        lst = sorted(counts_dict.keys())
        # length = 
        print(counts, counts_dict, lst, quantity)
        while quantity:
            q = quantity.pop()
            index = bisect_left(lst, q)
            if index == len(lst):
                return False

            v = lst[index]
            print(q, index, v, lst)
            counts_dict[v] -= 1
            if counts_dict[v] == 0:
                lst.remove(v)
            if v > q:
                counts_dict[v-q] += 1
                if v-q not in lst:
                    insort(lst, v-q)
        return True

from typing import List
from collections import Counter
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
        TLE
        """
        def dfs(i):
            if i == len_q:
                self.res = True
                return
            for j in range(len_n):
                v = lst[j]
                if v >= quantity[i]:
                    lst[j] = v - quantity[i]
                    dfs(i+1)
                    lst[j] = v


        quantity.sort()
        counts = Counter(nums)
        lst = list(counts.values())
        len_q = len(quantity)
        len_n = len(lst)
        # print(quantity, lst)
        self.res = False
        dfs(0)
        return self.res

from typing import List
from collections import Counter
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        def dfs(i):
            if i == len_q:
                self.res = True
                return
            for j in range(len_n):
                v = lst[j]
                if v >= quantity[i]:
                    lst[j] = v - quantity[i]
                    dfs(i+1)
                    lst[j] = v


        quantity.sort(reverse = True)
        counts = Counter(nums)
        lst = sorted(list(counts.values()), reverse = True)
        while quantity and lst:
            if lst[-1] < quantity[-1]:
                lst.pop()
            elif lst[-1] == quantity[-1]:
                lst.pop()
                quantity.pop()
            else:
                break

        len_q = len(quantity)
        len_n = len(lst)
        # print(quantity, lst)
        self.res = False
        dfs(0)
        return self.res


# 作者：日沉云起
# 链接：https://leetcode-cn.com/circle/discuss/KDCdc0/view/OWGkwf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def canDistribute(self, nums: List[int], q: List[int]) -> bool:
        c=list(Counter(nums).values())
        m,n=len(q),len(c)
        @lru_cache(None)
        def dfs(p,t,visit):#遍历到c[p]这个位置，且c[p]分配后剩余的值为t，visit[i]==1则表示quantity[i]已分配过
            if p==n:
                return 0
            ans=dfs(p+1,c[p+1] if p+1<n else 0,visit)
            for i in range(m):
                if t>=q[i] and ((visit>>i)&1)==0:
                    ans=max(ans,1+dfs(p,t-q[i],visit|(1<<i)))
            return ans
        return dfs(0,c[0],0)==m


from typing import List
from functools import lru_cache 
from collections import Counter
class Solution:
    def canDistribute(self, nums: List[int], q: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, rmd, visit_q):
            if i == len_l:
                return 0
            # print(i, rmd, visit_q)
            if i+1 == len_l:
                res = 0
            else:
                res = dp(i+1, lst[i+1], visit_q)
            for j in range(len_q):
                if (visit_q>>j)&1 == 0 and rmd >= q[j]:
                    res = max(res, 1+dp(i, rmd-q[j], visit_q|(1<<j)))
            return res


        counts = Counter(nums)
        lst = list(counts.values())
        len_l, len_q = len(lst), len(quantity)
        # print(lst, q)
        return dp(0, lst[0], 0) == len_q


# https://leetcode.com/problems/distribute-repeating-integers/discuss/935414/Python-Backtracking
from collections import Counter
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = Counter(nums)
        m = len(quantity)
        # we only need at most m different numbers, so we choose the ones which are most abundant
        left = sorted(c.values())[-m:]
        
        # If the customer with most quantity required can't be fulfilled, we don't need to go further and answer will be false
        quantity.sort(reverse=True)
        
        def func(left, quantity, customer):
            if customer == len(quantity):
                return True
            
            for i in range(len(left)):
                if left[i] >= quantity[customer]:
                    left[i] -= quantity[customer]
                    if func(left, quantity, customer+1):
                        return True
                    left[i] += quantity[customer]
            return False
        
        return func(left, quantity, 0)

S = Solution()
nums = [1,2,3,4]
quantity = [2]
print(S.canDistribute(nums, quantity))
nums = [1,2,3,3]
quantity = [2]
print(S.canDistribute(nums, quantity))
nums = [1,1,2,2]
quantity = [2,2]
print(S.canDistribute(nums, quantity))
nums = [1,1,2,3]
quantity = [2,2]
print(S.canDistribute(nums, quantity))
nums = [1,1,1,1,1]
quantity = [2,3]
print(S.canDistribute(nums, quantity))
nums = [154,533,533,533,154,154,533,154,154]
quantity =[3,2,2,2]
print(S.canDistribute(nums, quantity))
# # 输出：
# # false
# # 预期结果：
# # true
nums = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30,31,31,32,32,33,33,34,34,35,35,36,36,37,37,38,38,39,39]
quantity = [2,2,2,2,2,2,2,2,2,2]
print(S.canDistribute(nums, quantity))

nums = [1,1,2,2,1]
quantity = [2,3]
print(S.canDistribute(nums, quantity))
