"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 1E8]
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        wrong answer
        """
        digits_list = [int(s) for s in list(str(num))]
        n = len(digits_list)
        l,r = 0, n-1
        max_d = max(digits_list)
        while l < n-1 and digits_list[l] == max_d:
            l += 1
        while r > l and digits_list[r] != max_d:
            r -= 1
        # print(l,r)
        digits_list[l], digits_list[r] = digits_list[r], digits_list[l]
        return int(''.join(str(i) for i in digits_list))


class Solution:
        """
        wrong answer
        """
    def maximumSwap(self, num: int) -> int:
        digits = [int(s) for s in list(str(num))]
        stack = [0] #add a infinite num to stack
        n = len(digits)
        l, r = 0, None
        r_max = float('-inf')
        for i in range(1,n):
            # print(digits[i],r_max,stack)
            if stack and digits[i] <= digits[l]:
                stack.append(i) #decreasing value in stack, no need to swap
                l = i
            else:
                if digits[i] >= r_max: #larger than current r_max
                    r = i
                    r_max = digits[i]
                while stack and digits[r] > digits[l]:
                    l = stack.pop()
            print(digits[i], digits[l],stack)
            # ,digits[r]    
        if r is not None and l < r:
            digits[l], digits[r] = digits[r], digits[l]
        print(digits[l], digits[r], digits)
        return int(''.join(str(i) for i in digits))
            
        
class Solution:
    """
    right answer
    """
    def maximumSwap(self, num: int) -> int:
        digits = [int(s) for s in list(str(num))]
        stack = [0]
        n = len(digits)
        l, l_min, r, r_max = 0, digits[0], None, float('-inf')
        for i in range(1,n):
            if stack and digits[i] <= l_min:
                stack.append(i)
                l_min = digits[i] #the nums smaller than r_max will be append to stack, but not counted as l
            else:
                if digits[i] >= r_max:
                    r_max = digits[i]
                    r = i
                while stack and digits[r] > digits[stack[-1]]:
                    l = stack.pop()
                    l_min = digits[l]

        if r is not None and l < r:
            digits[l], digits[r] = digits[r], digits[l]
        return int(''.join(str(i) for i in digits))
                


class Solution:
    """
    right answer
    """
    def maximumSwap(self, num: int) -> int:
        digits = [int(s) for s in list(str(num))]
        last_index_of_v = {v:i for i,v in enumerate(digits)}
        for i,v in enumerate(digits):
            for j in range(9,v,-1):
                if last_index_of_v.get(j,-1) > i:
                    # print(i, last_index_of_v[j])
                    digits[i], digits[last_index_of_v[j]] = digits[last_index_of_v[j]], digits[i]
                    return int(''.join(map(str, digits)))
        return num


S = Solution()
num = 2736
print(S.maximumSwap(num))
num = 9973
print(S.maximumSwap(num))
num = 1
print(S.maximumSwap(num))
num = 98368
print(S.maximumSwap(num))
# """
# Output
# 98368
# Expected
# 98863
# """

num = 120
print(S.maximumSwap(num))
# Output
# 120
# Expected
# 210
num = 100
print(S.maximumSwap(num))
num = 1993
print(S.maximumSwap(num))
"""
Output
9193
Expected
9913
"""
num = 6565
# Output
# 6565
# Expected
# 6655
print(S.maximumSwap(num))