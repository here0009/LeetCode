"""
Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
 

Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_list, y_list = [], []
        total_set = set()
        tmp_x, tmp_y = 1, 1
        
        if x == 1:
            x_list = [x]
        else:
            while  tmp_x < bound:
                x_list.append(tmp_x)
                tmp_x *= x

        if y == 1:
            y_list = [y]
        else:
            while  tmp_y < bound:
                y_list.append(tmp_y)
                tmp_y *= y
        # print(x_list)
        # print(y_list)
        for i in x_list:
            for j in y_list:
                if i + j <= bound:
                    total_set.add(i+j)
                else:
                    break
        return list(total_set)

s = Solution()
x = 2
y = 3
bound = 10
print(s.powerfulIntegers(x,y,bound))
x = 3
y = 5
bound = 15
print(s.powerfulIntegers(x,y,bound))
x = 1
y = 1
bound = 2
print(s.powerfulIntegers(x,y,bound))