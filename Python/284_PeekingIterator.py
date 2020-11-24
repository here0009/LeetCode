"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""


# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        iterator is not node, once you call next, the iterator advances
        """
        self.iter = iterator
        self.tmp = None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.tmp:
            return self.tmp
        if self.iter.hasNext():
            self.tmp = self.iter.next()
            return self.tmp
        else:
            return None

    def next(self):
        """
        :rtype: int
        """
        res = self.peek()
        if self.iter.hasNext():
            self.tmp = self.iter.next()
        else:
            self.tmp = None
        return res
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.tmp:
            return True
        return self.iter.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


"""Test Case
input_list = ["PeekingIterator","hasNext","peek","peek","next","next","peek","peek","next","hasNext","peek","hasNext","next","hasNext"]
[[[1,2,3,4]],[],[],[],[],[],[],[],[],[],[],[],[],[]]
Output
[null,true,1,1,1,2,3,3,3,false,4,false,4,false]
Expected
[null,true,1,1,1,2,3,3,3,true,4,true,4,false]

["PeekingIterator","next","peek","next","next","hasNext"]
[[[1,2,3]],[],[],[],[],[]]
"""