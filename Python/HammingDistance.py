class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x^y
        counts = 0
        # print(z)
        while (z>0):
            i = z%2
            # print(i)
            z = int(z/2)
            counts += i
        return int(counts)

s = Solution()
print(s.hammingDistance(1,4))