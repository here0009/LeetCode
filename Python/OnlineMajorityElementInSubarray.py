"""
Implementing the class MajorityChecker, which has the following API:

MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
int query(int left, int right, int threshold) has arguments such that:
0 <= left <= right < arr.length representing a subarray of arr;
2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least threshold times, or -1 if no such element exists.

 

Example:

MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2
 

Constraints:

1 <= arr.length <= 20000
1 <= arr[i] <= 20000
For each query, 0 <= left <= right < len(arr)
For each query, 2 * threshold > right - left + 1
The number of queries is at most 10000
"""

from collections import defaultdict
import bisect
class MajorityChecker:
    def __init__(self, arr):
        self.arr = arr
        self.arr_index_dict = defaultdict(list)
        for i, v in enumerate(arr):
            self.arr_index_dict[v].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            num = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.arr_index_dict[num], left)
            r = bisect.bisect_right(self.arr_index_dict[num], right)
            if r - l >= threshold:
                return num
        return -1


import numpy as np
class MajorityChecker:
    def __init__(self, arr):
        self.arr = np.array(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        c = np.bincount(self.arr[left:right+1])
        x = np.argmax(c)
        return x if c[x] >= threshold else -1

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.loc = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.loc[n].append(i)    
        self.nums = sorted(self.loc.keys(), key = lambda n: len(self.loc[n]), reverse=True)
        
    def query(self, left: int, right: int, threshold: int) -> int:
        for n in self.nums:
            if len(self.loc[n]) < threshold: return -1
            l, r = bisect.bisect_left(self.loc[n], left), bisect.bisect_right(self.loc[n], right)
            if r - l >= threshold: return n
        return -1

# Your MajorityChecker object will be instantiated and called as such:
majorityChecker = MajorityChecker([1,1,2,2,1,1]);
print(majorityChecker.query(0,5,4))
print(majorityChecker.query(0,3,3))
print(majorityChecker.query(2,3,2))