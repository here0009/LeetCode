"""
Implement the class ProductOfNumbers that supports two methods:

1. add(int num)

Adds the number num to the back of the current list of numbers.
2. getProduct(int k)

Returns the product of the last k numbers in the current list.
You can assume that always the current list has at least k numbers.
At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 

Constraints:

There will be at most 40000 operations considering both add and getProduct.
0 <= num <= 100
1 <= k <= 40000
"""
from functools import lru_cache
class ProductOfNumbers_1:
    """
    Time Limit Exceeded
    """
    def __init__(self):
        self.numbers = [0]
        self.length = 0
        self.products = [1]
        self.zeros = set() #if there is any zeros in the last k elemnts, you can just return 0, and do not need to store the positions of zeros

    def add(self, num: int) -> None:
        
        self.numbers.append(num)
        if self.products[-1] != 0:
            self.products.append(self.products[-1]*num)
        else:
            self.zeros.add(self.length) #0 indexes
            self.products.append(num)
        self.length += 1


    def getProduct(self, k: int) -> int:

        @lru_cache(None)
        def dummy(length,k):
            if self.zeros & set(range(length-k+1, length)):
                return 0
            else:
                if self.products[length-k] != 0:
                    return self.products[length]//self.products[length-k]
                else:
                    return self.products[length]

        return dummy(self.length, k)
        
class ProductOfNumbers:
    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1]*num)


    def getProduct(self, k: int) -> int:
        length = len(self.products)-1
        if length-k < 0:
            return 0
        else:
            return self.products[length]//self.products[length-k]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3);        
obj.add(0);        
obj.add(2);        
obj.add(5);        
obj.add(4);        
print(obj.getProduct(2)); 
print(obj.getProduct(3)); 
print(obj.getProduct(4)); 
obj.add(8);        
print(obj.getProduct(2)); 