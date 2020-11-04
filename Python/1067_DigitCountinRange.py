"""
Given an integer d between 0 and 9, and two positive integers low and high as lower and upper bounds, respectively. Return the number of times that d occurs as a digit in all integers between low and high, including the bounds low and high.
 

Example 1:

Input: d = 1, low = 1, high = 13
Output: 6
Explanation: 
The digit d=1 occurs 6 times in 1,10,11,12,13. Note that the digit d=1 occurs twice in the number 11.
Example 2:

Input: d = 3, low = 100, high = 250
Output: 35
Explanation: 
The digit d=3 occurs 35 times in 103,113,123,130,131,...,238,239,243.
 

Note:

0 <= d <= 9
1 <= low <= high <= 2×10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/digit-count-in-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        """
        wrong answer
        """
        res = 0
        power = 0
        while high or low:
            high, rmd_high = divmod(high, 10)
            low, rmd_low = divmod(low, 10)
            res += (high - low + (rmd_high > d) + (rmd_low == d))*10**power
            power += 1
            print(high, low, res)
        return res
 

'''
用数位dp的思想来解决, 思维有一点点绕
首先把问题拆解一下，题目求的是low和high之间的数字中d出现的次数
可以分别求小于等于high的数字中d出现次数以及小于等于low-1的数字中
d出现的次数，然后把两个次数做减法得出答案

下面问题是怎么求小于等于n的数字中，d数字再数位上出现的次数？
先把n的每一位拆开，变成
data[0], data[1], ....... data[m] 其中data[m]是最高位的数字

那某一个小于等于n的数值的每一个数位都会收到data的限制，只能选取某些
特定的值，才能保持小于等于n

假设现在要凑一个小于等于n的数字data_lower[0], data_lower[1], .... data_lower[m]

定义一个三维的dp状态如下
dp[pos][higher_all_zero][higher_all_max]
表示的含义是data_lower[0], data_lower[1], ... data_lower[pos] 所有可能的合法组合中
能累计的数字d的个数

data_lower[0:pos+1]的组合是否合法需要看比pos位数高的那些位选择的情况，higher_all_zero
表示高于pos的那些位是不是全部都选了0，如果高位都选了0，当前这一位也选0的话，那当前这一位上的0
是不能算在d的计数里面的(如果d是0的话)，因为高位上连续的前导0实际上是没有出现在数字里面的

higher_all_max表示的是比pos高的那些为是不是都选择了data[pos+1], data[pos+2], .... data[m]
这些值，如果都选了这些值，当前这一位不可能选比data[pos]大的值了，如果选了不满足data_lower < data
否则当前这一位候选值可以是0-9

所以判断组合是否合法的时候，需要这两个维度的flag, dp状态就多了两个标志维度

最终的答案就是dp[m][True][True]

'''

# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/digit-count-in-range/solution/python-shu-wei-dp-ji-yi-hua-di-gui-shi-xian-jian-d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from functools import lru_cache
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        # 数字转成位数序列
        def data2bits(n):
            ans = []
            while n:
                ans.append(n % 10)
                n //= 10
            return tuple(ans)


        target_val = d

        # higher_cnt 表示比pos高的位已经累计的target_val的计数, 这里记忆化递归枚举可能的数位组合，返回所有可能的数位组合中target_val出现次数
        @lru_cache(None)
        def dfs(pos, higher_all_zero, higher_all_max, higher_cnt, data):

            if pos == -1:
                return higher_cnt

            up_bound = data[pos] if higher_all_max else 9
            count = 0
            for cur_val in range(up_bound+1):       # 枚举当前数位上可能的数值
                new_higher_cnt = higher_cnt + 1 if cur_val == target_val and not (cur_val == 0 and higher_all_zero) else higher_cnt
                count += dfs(pos-1, higher_all_zero and cur_val == 0, higher_all_max and cur_val == data[pos], new_higher_cnt, data)

            return count

        data = data2bits(high)
        val1 = dfs(len(data)-1, True, True, 0, data)
        data = data2bits(low-1)
        val2 = dfs(len(data) - 1, True, True, 0, data)
        return val1 - val2


# 作者：trojanmaster
# 链接：https://leetcode-cn.com/problems/digit-count-in-range/solution/python3dai-ma-zhu-wei-tong-ji-by-trojanmaster/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from collections import Counter
class Solution:
    def digitsCount(self, d, low, high):
        edge = Counter(str(low))[str(d)]
        if low == high:
            return edge
        ans = edge + self.count(high, d) - self.count(low, d)
        return ans  

    def count(self, limit, d):
        num_str = str(limit)
        res = 0
        for i in range(len(num_str)-1, -1, -1):
            if d == int(num_str[i]):
                part1 = int(num_str[:i]) * pow(10, len(num_str)-(i+1)) if i != 0 else 0
                part2 = 1 * (1 + int(num_str[i+1:])) if i != len(num_str)-1 else 1
                res = res + part1 + part2
            elif d < int(num_str[i]):
                prev = 1 + int(num_str[:i]) if i != 0 else 1
                part1 = prev * pow(10, len(num_str)-(i+1))
                res = res + part1
            else:
                part1 = int(num_str[:i]) * pow(10, len(num_str)-(i+1)) if i != 0 else 0
                res = res + part1
        if d == 0:
            for i in range(1,len(num_str)):
                res = res - pow(10, i)
        return res


# 作者：mikeliu
# 链接：https://leetcode-cn.com/problems/digit-count-in-range/solution/dui-mei-wei-ji-shu-by-mikeliu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def digitsCount(self, d, low, high):
        ans=0
        sd,slow,shigh=str(d),'000000000'+str(low),str(high)
        for k in range(len(shigh)):
            unit=10**k
            mult=1+high//(unit*10)-low//(unit*10)
            if slow[-k-1]>=sd:
                mult-=1
            if shigh[-k-1]<=sd:
                mult-=1
            ans+=mult*unit
            if slow[-k-1]==sd and (d!=0 or low>=unit):
                ans+=unit-low%unit
            if shigh[-k-1]==sd:
                ans+=high%unit+1
        return ans


# 作者：fang-tou-shi-live
# 链接：https://leetcode-cn.com/problems/digit-count-in-range/solution/wo-lai-xie-yi-ge-shu-xue-fa-qing-xi-ming-liao-by-f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution {
    public int digitsCount(int d, int low, int high) {
        return (int)(count(d,high)-count(d,low-1));
    }

    private long count(int d,int n){
        long res =0;
        for(long i=1;i<=n;i*=10){
            long dvid = i*10;
            // 高位
            long high = n/dvid;
            // 当前位
            long cur = n/i%10;
            // 低位
            long low = n%i;
            if(cur>d){
                res+=(high+1)*i;
            }else if(cur<d){
                res+=high*i;
            }else{
                res+=high*i+low+1;
            }
            // 如果d=0会特殊处理，需要减掉当前位数，因为当前位不能以0开头
            if(d==0){
                res-=i;
            }
        }
        return res;
    }
}

"""

class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def calc(num, d):
            """
            return the counts of i that have a digit 'd' and 0 < i <= num
            """
            power = 1
            res = 0
            while power <= num:
                high = num //(power*10)
                curr = num // power % 10
                rmd = num % power
                if curr > d:
                    res += (high+1)*power  # 0 ~ high
                elif curr < d:
                    res += high*power   # 0 ~ high-1
                else:
                    res += high*power + rmd + 1  # 0 ~ high-1 + 0 ~ rmd
                if d == 0:
                    res -= power
                # print(high, curr, rmd, power, res)
                power *= 10
            # print(num, res)
            return res

        return calc(high, d) - calc(low-1, d)



S = Solution()
d = 1
low = 1
high = 13
print(S.digitsCount(d, low, high))
d = 3
low = 100
high = 250
print(S.digitsCount(d, low, high))