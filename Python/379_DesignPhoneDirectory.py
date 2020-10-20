"""
Design a Phone Directory which supports the following operations:

 

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
 

Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
 

Constraints:

1 <= maxNumbers <= 10^4
0 <= number < maxNumbers
The total number of call of the methods is between [0 - 20000]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-phone-directory
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.available = set(range(maxNumbers))
        self.visited = set()

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.available:
            num = self.available.pop()
            self.visited.add(num)
            return num
        return -1


    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.available


    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.visited:
            self.visited.remove(number)
            self.available.add(number)




# Your PhoneDirectory object will be instantiated and called as such:
obj = PhoneDirectory(maxNumbers)
param_1 = obj.get()
param_2 = obj.check(number)
obj.release(number)