class Solution(object):
    def decodeAtIndex(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        print(size)
        for c in reversed(S):
            K %= size
            print(K)
            print(size)
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1

s = Solution()
input_str = "leet2code3"
K = 10
print(s.decodeAtIndex(input_str, K))