"""
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""
class Solution_1:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pushed_index = 0
        for popped_element in popped:
            while (pushed_index < len(pushed)) and (popped_element not in stack):
                stack.append(pushed[pushed_index])
                pushed_index += 1
            # print(stack)
            if stack.pop() != popped_element:
                return False
        return True

class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        """
        Solution_1 can pass the test, but "popped_element not in stack" is somehow not efficient, it can be optimized
        """
        stack = []
        poped_index = 0
        for pushed_element in pushed:
            stack.append(pushed_element)
            while stack and stack[-1] == popped[poped_index]:
                poped_index += 1
                stack.pop()
        return poped_index == len(popped)





s = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(s.validateStackSequences(pushed, popped))

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(s.validateStackSequences(pushed, popped))

pushed = []
popped = []
print(s.validateStackSequences(pushed, popped))

pushed = [0]
popped = [0]
print(s.validateStackSequences(pushed, popped))

pushed = [0]
popped = [1]
print(s.validateStackSequences(pushed, popped))