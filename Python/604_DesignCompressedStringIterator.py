"""Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

Implement the StringIterator class:

next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
 

Example 1:

Input
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

Explanation
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True
 

Constraints:

1 <= compressedString.length <= 1000
compressedString consists of lower-case an upper-case English letters and digits.
The number of a single character repetitions in compressedString is in the range [1, 10^9]
At most 100 calls will be made to next and hasNext.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-compressed-string-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class StringIterator:

    def __init__(self, compressedString: str):
        self.letters = []
        self.vals = []
        index = 0
        length = len(compressedString)
        curr = ''
        while index < length:
            c = compressedString[index]
            if c.isdigit():
                curr += c
            else:
                if curr:
                    self.vals.append(int(curr))
                    curr = ''
                self.letters.append(c)
            index += 1
        if curr:
            self.vals.append(int(curr))
        self.index = 0
        self.length = len(self.letters)
        self.count = 0
        # print(self.vals)
        # print(self.letters)

    def next(self) -> str:
        if self.hasNext():
            v = self.letters[self.index]
            self.count += 1
            return v
        return ' '

    def hasNext(self) -> bool:
        while self.index < self.length and self.vals[self.index] == self.count:
            self.index += 1
            self.count = 0
        return self.index < self.length



# Your StringIterator object will be instantiated and called as such:
obj = StringIterator("L1e3t1C1o1d1e1")

print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.next())