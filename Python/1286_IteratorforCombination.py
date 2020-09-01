"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid
"""


from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res = []
        for s in combinations(characters, combinationLength):
            self.res.append(''.join(s))
        self.length = len(self.res)
        self.index = 0

    def next(self) -> str:
        if self.index < self.length:
            elem = self.res[self.index]
            self.index += 1
            return elem


    def hasNext(self) -> bool:
        return self.index < self.length


# https://leetcode.com/problems/iterator-for-combination/discuss/451260/python-using-generator
class CombinationIterator:
    def __init__(self, chars: str, comblen: int):
        self.generator = self.genNext(chars, [], comblen, 0)
        self.last, self.end = None, chars[-comblen:]
        
    def genNext(self, chars, path, coml, st):
        if coml == 0: yield ''.join(path); return
        for i in range(st, len(chars)):
            yield from self.genNext(chars, path+[chars[i]], coml-1, i+1)

    def next(self) -> str:
        self.last = next(self.generator)
        return self.last

    def hasNext(self) -> bool:
        return self.last != self.end


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def combinations(cur, idx):
            if len(cur) == combinationLength:
                yield ''.join(cur)
                return
            for i in range(idx, len(characters)):
                cur.append(characters[i])
                yield from combinations(cur, i + 1)
                cur.pop()
        self.combos = combinations([], 0)
        self.current = True
        self.hasNextCalled = False
                
        

    def next(self) -> str:
        if self.hasNext():
            self.hasNextCalled = False
            return self.current
        

    def hasNext(self) -> bool:
        if self.current and not self.hasNextCalled:
            self.hasNextCalled = True
            self.current = next(self.combos, False)
        return bool(self.current)

# Your CombinationIterator object will be instantiated and called as such:
iterator = CombinationIterator("abc", 2);
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())