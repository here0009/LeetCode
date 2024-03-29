"""
设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。

它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
import heapq
class LRUCache:
    """
    wrong answer 17/18
    """

    def __init__(self, capacity: int):

        self.cache = dict()
        self.capacity = capacity
        self.idx = 0
        self.pq = []
        self.counts = Counter()


    def get(self, key: int) -> int:
        self.idx += 1
        self.counts[key] += 1
        heapq.heappush(self.pq, (self.idx, key))
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.get(key)
        if len(self.cache) > self.capacity:
            while self.pq:
                if self.counts[self.pq[0][1]] == 1:
                    break
                _, _k = heapq.heappop(self.pq)
                if self.counts[self.pq[0][1]] == 0:
                    continue
                self.counts[_k] -= 1
            _, rm_key = heapq.heappop(self.pq)
            self.counts[rm_key] -= 1
            if rm_key in self.cache:
                del self.cache[rm_key]


from collections import Counter
import heapq
class LRUCache:

    def __init__(self, capacity: int):

        self.cache = dict()
        self.capacity = capacity
        self.idx = 0
        self.pq = []
        self.counts = Counter()


    def get(self, key: int) -> int:
        self.idx += 1
        self.counts[key] += 1
        heapq.heappush(self.pq, (self.idx, key))
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.get(key)
        if len(self.cache) > self.capacity:
            while self.pq:
                if self.counts[self.pq[0][1]] == 1 and self.pq[0][1] in self.cache:
                    break
                _, _k = heapq.heappop(self.pq)
                if self.counts[self.pq[0][1]] == 0:
                    continue
                self.counts[_k] -= 1
            _, rm_key = heapq.heappop(self.pq)
            self.counts[rm_key] -= 1
            del self.cache[rm_key]


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/lru-cache-lcci/solution/lruhuan-cun-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)