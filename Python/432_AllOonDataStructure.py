"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""


from collections import defaultdict
class AllOne:
    """
    wrong answer
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = defaultdict(set)
        self.max_val, self.min_val = -float('inf'), float('inf')
        self.keys = dict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keys:
            self.keys[key] += 1
        else:
            self.keys[key] = 1
        v = self.keys[key]
        self.vals[v].add(key)
        self.max_val = max(self.max_val, v)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keys:
            v = self.keys[key]
            self.vals[v].remove(key)
            v -= 1
            if v == 1:
                del self.keys[key]
            else:
                self.keys[key] = v
                self.vals[v].add(key)
                self.min_val = min(self.min_val, v)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_val in self.vals and len(self.vals[self.max_val]) > 0:
            key = self.vals[self.max_val].pop()
            self.vals[self.max_val].add(v)
            return key
        return ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.min_val in self.vals and len(self.vals[self.min_val]) > 0:
            key = self.vals[self.min_val].pop()
            self.vals[self.min_val].add(v)
            return key
        return ''


from collections import Counter, defaultdict
class AllOne:
    """
    use a Counter to record the counts of key
    use defaultdict(set) to record the counts[v]: {keys}
    use a min_v, max_v to record the min_counts and max_counts
    update min_v, max_v at each inc and dec operation
    TLE, still not O(n) to get min_v
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = Counter()
        self.vals = defaultdict(set)
        self.max_v = 0
        self.min_v = 0

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.counts[key] += 1
        v = self.counts[key]
        self.vals[v].add(key)
        if v > 1:
            self.vals[v - 1].remove(key)
            if not self.vals[v - 1]:
                del self.vals[v - 1]
        if v > self.max_v:
            self.max_v = v
        if v == 1:
            self.min_v = 1
        else:
            if v - 1 == self.min_v and self.min_v not in self.vals: # the last key of self.min_v
                self.min_v += 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.counts:
            self.counts[key] -= 1
            v = self.counts[key]
            self.vals[v + 1].remove(key)
            if not self.vals[v + 1]:
                del self.vals[v + 1]
            if v == 0:
                del self.counts[key]
            else:
                self.vals[v].add(key)
            if v + 1 == self.max_v and v + 1 not in self.vals:
                self.max_v -= 1
            if v in self.vals and self.min_v > v:
                self.min_v = v
            else:
                while self.min_v not in self.vals and self.min_v < self.max_v:
                    self.min_v += 1


    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_v == 0:
            return ''
        key = self.vals[self.max_v].pop()
        self.vals[self.max_v].add(key)
        return key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.min_v == 0:
            return ''
        key = self.vals[self.min_v].pop()
        self.vals[self.min_v].add(key)
        return key


from collections import Counter, defaultdict, deque
class AllOne:
    """
    use a deque to store the vals, finaly, get it down
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = Counter()
        self.vals = defaultdict(set)
        self.dq = deque([])

    def _delete(self, key, val):
        # print('_delete', key, val, self.vals)
        if self.counts[key] == 0:
            del self.counts[key]
        if val in self.vals and key in self.vals[val]:
            self.vals[val].remove(key)
        if len(self.vals[val]) == 0:
            del self.vals[val]
        # print('_delete', key, val, self.vals)
        # if self.dq and val == self.dq[0] and val not in self.vals:
        #     self.dq.popleft()
        # if self.dq and val == self.dq[-1] and val not in self.vals:
        #     self.dq.pop()
        while self.dq and self.dq[-1] not in self.vals:
            self.dq.pop()
        while self.dq and self.dq[0] not in self.vals:
            self.dq.popleft()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # print('inc, key', self.dq, self.vals, self.counts)
        self.counts[key] += 1
        v = self.counts[key]
        self.vals[v].add(key)
        if v > 1:
            self._delete(key, v - 1)
        if not self.dq or v > self.dq[-1]:
            self.dq.append(v)
        elif v < self.dq[0]:
            self.dq.appendleft(v)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        # print('dec, key', self.dq, self.vals, self.counts)
        if key in self.counts:
            self.counts[key] -= 1
            v = self.counts[key]
            self._delete(key, v + 1)
            if v != 0:
                self.vals[v].add(key)
                if not self.dq or v < self.dq[0]:
                    self.dq.appendleft(v)
                elif v > self.dq[-1]:
                    self.dq.append(v)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        # print('getMaxKey', self.dq, self.vals, self.counts)
        if not self.dq:
            return ''
        v = self.dq[-1]
        key = self.vals[v].pop()
        self.vals[v].add(key)
        return key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        # print('getMinKey', self.dq, self.vals, self.counts)
        if not self.dq:
            return ''
        v = self.dq[0]
        key = self.vals[v].pop()
        self.vals[v].add(key)
        return key



from collections import Counter, defaultdict, deque
class AllOne:
    """
    use a deque to store the vals, finaly, get it down
    try to optimize it
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = Counter()
        self.vals = defaultdict(set)
        self.dq = deque([])

    def _updateDq(self, v):
        if not self.dq or v > self.dq[-1]:
            self.dq.append(v)
        elif v < self.dq[0]:
            self.dq.appendleft(v)

    def _delete(self, key, val):
        # print('_delete', key, val, self.vals)
        if self.counts[key] == 0:
            del self.counts[key]
        if val in self.vals and key in self.vals[val]:
            self.vals[val].remove(key)
        if not self.vals[val]:
            del self.vals[val]
        while self.dq and self.dq[-1] not in self.vals:
            self.dq.pop()
        while self.dq and self.dq[0] not in self.vals:
            self.dq.popleft()


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # print('inc, key', self.dq, self.vals, self.counts)
        self.counts[key] += 1
        v = self.counts[key]
        self.vals[v].add(key)
        if v > 1:
            self._delete(key, v - 1)
        self._updateDq(v)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        # print('dec, key', self.dq, self.vals, self.counts)
        if key in self.counts:
            self.counts[key] -= 1
            v = self.counts[key]
            self._delete(key, v + 1)
            if v != 0:
                self.vals[v].add(key)
                self._updateDq(v)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        # print('getMaxKey', self.dq, self.vals, self.counts)
        if not self.dq:
            return ''
        v = self.dq[-1]
        key = self.vals[v].pop()
        self.vals[v].add(key)
        return key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        # print('getMinKey', self.dq, self.vals, self.counts)
        if not self.dq:
            return ''
        v = self.dq[0]
        key = self.vals[v].pop()
        self.vals[v].add(key)
        return key


from collections import Counter, defaultdict, deque
class AllOne:
    """
    use a deque to store the vals, finally, get it down
    try to optimize it
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = Counter()
        self.vals = defaultdict(set)
        self.dq = deque([])

    def _insert(self, key, val):
        if val > 0:
            self.vals[val].add(key)
            if not self.dq:
                self.dq.append(val)
            elif val > self.dq[-1]:
                self.dq.append(val)
            elif val < self.dq[0]:
                self.dq.appendleft(val)

    def _delete(self, key, val):
        # print('_delete', key, val, self.vals)
        if val in self.vals and key in self.vals[val]:
            self.vals[val].remove(key)
        while self.dq and not self.vals[self.dq[-1]]:
            self.dq.pop()
        while self.dq and not self.vals[self.dq[0]]:
            self.dq.popleft()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # print('inc, key', self.dq, self.vals, self.counts)
        pre_v = self.counts[key]
        v = pre_v + 1
        self.counts[key] = v
        self._delete(key, pre_v)
        self._insert(key, v)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        # print('dec, key', self.dq, self.vals, self.counts)
        if key in self.counts:
            pre_v = self.counts[key]
            v = pre_v - 1
            self.counts[key] = v
            self._delete(key, pre_v)
            self._insert(key, v)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        # print('getMaxKey', self.dq, self.vals, self.counts)
        if not self.dq:
            return ''
        v = self.dq[-1]
        key = self.vals[v].pop()
        self.vals[v].add(key)
        return key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        # print('getMinKey', self.dq, self.vals, self.counts)
        if not self.dq:
            return ''
        v = self.dq[0]
        key = self.vals[v].pop()
        self.vals[v].add(key)
        return key



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()      
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Wrong Answer
# Details 
# Input
# ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
# [[],["hello"],["hello"],[],[],["leet"],[],[]]
# Output
# [null,null,null,"hello","hello",null,"hello","hello"]
# Expected
# [null,null,null,"hello","hello",null,"hello","leet"]


# Input
# ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
# [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
# Output
# [null,null,null,null,null,null,null,null,null,"a",null,"c",""]
# Expected
# [null,null,null,null,null,null,null,null,null,"a",null,"c","c"]


# ["AllOne","inc","inc","inc","inc","inc","dec","dec","getMaxKey","getMinKey"]
# [[],["a"],["b"],["b"],["b"],["b"],["b"],["b"],[],[]]


# https://leetcode.com/problems/all-oone-data-structure/discuss/91428/Python-solution-with-detailed-comments