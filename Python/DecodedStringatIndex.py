"""
Thoughts:
if store the repeat string in memory, it will be huge.
so we can store the repeat string in a list of tuple, like "leet2code3" can be stored as [(leet, 2), (code, 3)], so the total number of letters is counts = ((len(leet) * 2) + len(code)) * 3. 
counts  = (4*2 + 4) * 3 = 36
If the total number is larger than K, set K = 10. 
the letter is 10%36 = 10, 
size/=3 = 12
10%12 = 10
6 < 8, so 6%8 = 3
"""
class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        repeat_list = []
        repeat_s = ""
        repeat_time = 0
        counts = 0
        nums = "0123456789"
        for s in S:
            if s not in nums:
                repeat_s += s
                counts += 1
                if K == counts:
                    return s

            else:
                
                repeat_time = int(s)
                repeat_list.append((repeat_s, repeat_time))
                counts *= repeat_time
                if counts >= K:
                    return repeat_s[K%counts - 1]
                else:
                    
                    repeat_s = "" #set repeat_s to empty string

s = Solution()
input_str = "leet2code3"
K = 10
print(s.decodeAtIndex(input_str, K))

input_str = "ha22"
K = 5
print(s.decodeAtIndex(input_str, K))

input_str = "a2345678999999999999999"
K = 1
print(s.decodeAtIndex(input_str, K))

input_str = "y959q969u3hb22odq595"
K = 222280369
print(s.decodeAtIndex(input_str, K))