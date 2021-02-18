"""
Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

print(LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Sets or inserts the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be evicted.
Notice that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[None, None, None, 1, None, -1, 3, None, -1, 3, 4]

Explanation
print(LFUCache lfu = new LFUCache(2);
print(lfu.put(1, 1);
print(lfu.put(2, 2);
print(lfu.get(1);     # return 1
print(lfu.put(3, 3)   # evicts key 2
print(lfu.get(2);     # return -1 (not found)
print(lfu.get(3);     # return 3
print(lfu.put(4, 4)   # evicts key 1.
print(lfu.get(1);     # return -1 (not found)
print(lfu.get(3);     # return 3
print(lfu.get(4);     # return 4
 

Constraints:

0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.
 

Follow up: Could you do both operations in O(1) time complexity?
"""


from collections import Counter
import heapq
class LFUCache:

    def __init__(self, capacity: int):
        self.timestamp = 0
        self.pq = []  # record (count, timestamp, key)
        self.keys = dict()
        self.time = dict()
        self.counts = Counter()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            self.timestamp += 1
            self.counts[key] += 1
            self.time[key] = self.timestamp
            heapq.heappush(self.pq, (self.counts[key], self.time[key], key))
            # print(self.keys)
            return self.keys[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        self.timestamp += 1
        if len(self.keys) == self.capacity and key not in self.keys:  # pop the least recent used keys
            while self.pq and (self.pq[0][2] not in self.keys or self.pq[0][1] < self.time[self.pq[0][2]]):  # key not in keys or key have used after the timestamp
                heapq.heappop(self.pq)
            _, _, pre_key = heapq.heappop(self.pq)
            del self.keys[pre_key]
            del self.time[pre_key]
            del self.counts[pre_key]
        self.keys[key] = value
        self.time[key] = self.timestamp
        self.counts[key] += 1
        heapq.heappush(self.pq, (self.counts[key], self.time[key], key))


# Your LFUCache object will be instantiated and called as such:
lfu = LFUCache(2)
print(lfu.put(1, 1))
print(lfu.put(2, 2))
print(lfu.get(1))    # return 1
print(lfu.put(3, 3))   # evicts key 2
print(lfu.get(2))     # return -1 (not found)
print(lfu.get(3))     # return 3
print(lfu.put(4, 4))   # evicts key 1.
print(lfu.get(1))     # return -1 (not found)
print(lfu.get(3))     # return 3
print(lfu.get(4))     # return 4


# command = ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
# parameter = [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
# output = [None,None,None,2,1,2,None,None,3,2,-1,4]
# expected = [None,None,None,2,1,2,None,None,-1,2,1,4]

# for c, p, o, e in zip(command, parameter, output, expected):
#     print(c, p, o, e)

# ["LFUCache","put","get"]
# [[0],[0,0],[0]]


command = ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
parameter = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

output = [None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,14,None,None,18,None,None,11,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]

expected = [None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,14,None,None,18,None,None,11,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,-1,None,None,None,20,None,None,None,29,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
for c, p, o, e in zip(command, parameter, output, expected):
    print(c, p, o, e)