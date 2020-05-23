class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        Max_Number = 1E9+7
        lcm_AB = self.lcm(A,B)
        seq = dict()
        for i in range(1, lcm_AB//A + 1):
            seq[i*A] = 1
        for i in range(1, lcm_AB//B + 1):
            seq[i*B] = 1
        candidates = sorted([key for key in seq.keys()])
        magicalNumber = ((N-1)//len(candidates))*candidates[-1] + candidates[N%len(candidates)-1]
        return int(magicalNumber % Max_Number)

    def gcd(self, m, n):
        """
        return the greatest common divider of m and n
        """
        if n > m:
            m, n = n, m
        q = m%n
        if q == 0:
            return n
        else:
            return self.gcd(n,q)


    def lcm(self, m, n):
        """
        return the largest common multiplier of m and n
        """
        return m*n//self.gcd(m,n)

