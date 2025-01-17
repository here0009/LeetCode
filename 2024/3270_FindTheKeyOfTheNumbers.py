class Solution:
    
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        def encod4digit(num:int):
            return str(num)[:4].zfill(4)
        
        digit_lst = []
        c = 0
        e_nums = [encod4digit(i) for i in [num1, num2, num3]]
        for i in range(4):
            digit = min([int(e[3-i]) for e in e_nums])
            c, rmd = divmod(digit, 10)
            digit_lst.append(rmd + c)
        res = 0
        # print(digit_lst)
        for i, v in enumerate(digit_lst):
            res += v * 10**i
        return res


s = Solution()
num1 = 1
num2 = 10
num3 = 1000
print(s.generateKey(num1, num2, num3)) # 0
num1 = 987
num2 = 879
num3 = 798
print(s.generateKey(num1, num2, num3)) # 777
num1 = 1
num2 = 2
num3 = 3
print(s.generateKey(num1, num2, num3)) # 1