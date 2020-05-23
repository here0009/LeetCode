class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        else:
            n = haystack.find(needle)
            return n

s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("sdfsdfsdf", ""))