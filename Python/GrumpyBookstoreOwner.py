"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""
class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        length = len(customers)
        res = 0
        grumpy_customers = [grumpy[i]*customers[i] for i in range(length)]
        res = sum([customers[i] for i in range(length) if grumpy[i] == 0])
        
        tmp = sum(grumpy_customers[0:X])
        sum_X = tmp
        # print(res, grumpy_customers)

        for i in range(0,length-X):
            
            tmp = tmp - grumpy_customers[i] + grumpy_customers[i+X]
            sum_X = max(sum_X, tmp)
        res += sum_X
        return res

s = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(s.maxSatisfied(customers, grumpy, X))

customers = [3]
grumpy = [1]
X = 4
print(s.maxSatisfied(customers, grumpy, X))

customers = [4,10,10]
grumpy = [1,1,0]
X = 2
print(s.maxSatisfied(customers, grumpy, X))