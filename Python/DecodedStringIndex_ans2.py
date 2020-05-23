class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        for s in S:
            if s.isalpha():
                size += 1
            elif s.isdigit():
                size *= int(s)


        rev_S = reversed(S)
        for s in rev_S:
            K %= size
            if K % size == 0 and s.isalpha():
                return s
            if s.isdigit():
                size /= int(s)
            elif s.isalpha():
                size -= 1

s = Solution()
input_str = "leet2code3"
K = 10
print(s.decodeAtIndex(input_str, K))