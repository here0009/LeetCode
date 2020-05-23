"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

        

from random import randrange
class RandomizedSet_1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.set:
            self.set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        l = list(self.set) #it is O(n)
        if l:
            r = randrange(len(l))
        return l[r]


from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            pop_index = self.dict[val]
            last_val = self.list[-1]
            self.list[pop_index] = last_val
            self.dict[last_val] = pop_index
            self.list.pop()
            del self.dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:

randomSet = RandomizedSet()
print(randomSet.insert(1))
print(randomSet.remove(2))
print(randomSet.insert(2))
print(randomSet.getRandom())
print(randomSet.remove(1))
print(randomSet.insert(2))
print(randomSet.getRandom())
