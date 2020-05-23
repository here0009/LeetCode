"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array (nums, which contains initial elements from the stream. For each call to the method KthLargest.add, printreturn the element representing the kth largest element in the stream.)

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest KthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
class KthLargest_1:

    def __init__(self, k: int, nums):
        self.nums = sorted(nums, reverse = True)[:k]
        self.k = k
        # print(self.nums)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse = True)[:self.k]
        # print(self.nums)
        return self.nums[-1]

import heapq
from heapq import heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, val)
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
k = 3;
nums = [4,5,8,2];

obj = KthLargest(k, nums)


print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
