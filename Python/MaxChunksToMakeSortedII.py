"""
This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
"""


class Solution:
    """
    wrong ans for test case arr = [1,1,0,0,1]
    """
    def maxChunksToSorted(self, arr) -> int:
        s_arr = sorted(arr)
        arr_index_dict = dict()
        for i,v in enumerate(s_arr):
            if v not in arr_index_dict:
                arr_index_dict[v] = i
        print(arr_index_dict)
        currMax = 0
        res = 0
        for i,v in enumerate(arr):
            currMax = max(currMax, v)
            if arr_index_dict[currMax] <= i:
                res += 1
        return res

from collections import Counter
from collections import deque
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        a_counter = Counter(arr)
        dq = deque(sorted(a_counter.keys()))
        res = 0
        for n in arr:
            a_counter[n] -= 1
            while dq and a_counter[dq[0]] == 0:
                dq.popleft()
            # print(dq, n)
            if not dq or (len(dq) == 1 and n == dq[0]) or (dq[0] >= n and a_counter[n] == 0):
                res += 1
        return res


from collections import Counter
from collections import deque
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        if len(arr) == 1:
            return 1
        a_counter = Counter(arr)
        dq = deque(sorted(a_counter.keys()))
        res = 0
        pre = arr[0]
        counts = 1
        a_counter[pre] -= 1
        new_arr = arr[1:] + [float('inf')]
        for n in new_arr:
            if n == pre:
                counts += 1
            else:
                while dq and a_counter[dq[0]] == 0:
                    dq.popleft()
                if not dq or (dq[0] >= pre and a_counter[pre] == 0):
                    res += counts
                pre = n
                counts = 1
            # print(n,dq, res)
            a_counter[n] -= 1
        return res


from collections import Counter
from collections import deque
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        s_arr = sorted(arr)
        arr_index_dict = dict()
        for i,v in enumerate(s_arr):
            if v not in arr_index_dict:
                arr_index_dict[v] = i

        a_counter = Counter(arr)
        dq = deque(sorted(a_counter.keys()))
        print(arr)
        # print(arr_index_dict)
        currMax = 0
        res = 0
        for i,v in enumerate(arr):
            currMax = max(currMax, v)
            while dq and a_counter[dq[0]] == 0:
                dq.popleft()
            if arr_index_dict[currMax] <= i:
                res += 1
            a_counter[v] -= 1
        return res


class Solution:
    def maxChunksToSorted(self, arr) -> int:
        """
        because s_arr is sorted, so if sum(arr[:i]) == sum(s_arr[:i]), the elments in arr[:i] and s_arr[:i] are the same
        """
        s_arr = sorted(arr)
        tmp_s, tmp_a = 0, 0
        length = len(arr)
        res = 0
        for i in range(length):
            tmp_s += s_arr[i]
            tmp_a += arr[i]
            res += (tmp_s == tmp_a)
        return res


class Solution:
    """
    monotonic stack
    """
    def maxChunksToSorted(self, arr) -> int:
        stack = []
        for num in arr:
            max_num = num
            while stack and stack[-1] > num:
                max_num = max(stack.pop(), max_num)
            stack.append(max_num)
        return len(stack)


class Solution:
    def maxChunksToSorted(self, arr) -> int:

        l = len(arr)
        left_max, right_min = [arr[0]] * l, [arr[-1]] * l

        for i in range(1, l):
            left_max[i] = arr[i] if arr[i] > left_max[i - 1] else left_max[i - 1]
        for i in range(l - 2, -1, -1):
            right_min[i] = arr[i] if arr[i] < right_min[i + 1] else right_min[i + 1]

        # print(left_max)
        # print(right_min)
        count = 1
        for i in range(l - 1):
            if left_max[i] <= right_min[i + 1]:  # so we can split from i
                count += 1

        return count

S = Solution()
arr = [5,4,3,2,1]
print(S.maxChunksToSorted(arr))
arr = [2,1,3,4,4]
print(S.maxChunksToSorted(arr))
arr = [1,1,0,0,1]
print(S.maxChunksToSorted(arr))
arr = [2,1,3,4,1,4]
print(S.maxChunksToSorted(arr))
arr = [2,1,3,4,4,4,4]
print(S.maxChunksToSorted(arr))
# Output
# 3
# Expected
# 4
arr = [0,0,1,1,1]
print(S.maxChunksToSorted(arr))
# Output
# 4
# Expected
# 5

arr =[2,0,1]
print(S.maxChunksToSorted(arr))
# Output
# 2
# Expected
# 1