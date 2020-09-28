"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iii-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TwoSum:
    """
    TLE
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = set()
        self.twoSums = set()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.vals:
            self.twoSums.add(number*2)
        else:
            for v in self.vals:
                self.twoSums.add(v + number)
            self.vals.add(number)


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        return value in self.twoSums



from collections import Counter
class TwoSum:
    """
    in the test, add was called far more frequent than find, so use hash table and won't get TLE
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = Counter()


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.vals[number] += 1


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for v in self.vals:
            if value - v != v and value - v in self.vals:
                return True
            elif value - v == v and self.vals[v] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)