class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        len_x = len(str_x)
        for i in range(len_x):
            if str_x[i] != str_x[-1*(i+1)]:
                # print(str_x[i], str_x[-1*(i+1)])
                return False
        return True

s = Solution()
tests = [121, -121, 10]
for test in tests:
    print(s.isPalindrome(test))