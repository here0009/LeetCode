from typing import List


class Solution_w: # wrong answer
    def minimumCost(self, s: str) -> int:
        def get_cost(pre:int, end:int, length:int) -> int:
            dist = min(pre + 1, length - pre)
            print(pre, end, dist)
            return dist + (dist - (end - pre))
        
        def convert(input_str:str, target_c:chr) -> int:
            print('+'*15)
            res = 0
            length = len(input_str)
            idx, pre, end = 0, 0, 0
            flag = False
            while idx < length:
                if input_str[idx] != target_c:
                    if not flag:
                        flag = True
                        pre = idx
                else:
                    if flag:
                        end = idx
                        res += get_cost(pre, end, length)
                        flag = False
                idx += 1
                
            if flag:
                end = idx
                res += get_cost(pre, end, length)
            print(input_str, target_c, res)
            return res
        print('='*20)
        return min(convert(s, '1'), convert(s, '0'))

class Solution:
    def minimumCost(self, s: str) -> int:
        length = len(s)
        res = 0
        for i in range(1, length):
            if s[i] != s[i-1]:
                res += min(i, length - i)
        return res

sol = Solution()
s = '0011'
print('res', sol.minimumCost(s))
s = '010101'
print('res', sol.minimumCost(s))
s = "000000110"
print('res', sol.minimumCost(s))