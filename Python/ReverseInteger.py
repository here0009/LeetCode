class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_string = str(x)
        if x_string[0] == "-":
            negative = True
        else:
            negative = False
        if negative:
            x_string_reverse = x_string[1:][::-1]
        else:
            x_string_reverse = x_string[::-1]
        if negative:
            x_reversed = -1 * int(x_string_reverse)
        else:
            x_reversed = int(x_string_reverse)

        if outOfLimits(x_reversed):
            x_reversed = 0
        return x_reversed

def outOfLimits(num):
    '''
    return true if num is out of limits
    '''
    lower_limits = -2**31
    upper_limits = 2**31-1
    if num < lower_limits or num > upper_limits:
        return True
    else:
        return False


s = Solution()
print(s.reverse(123))
print(s.reverse(320))
print(s.reverse(-123))
print(s.reverse(1534236469))