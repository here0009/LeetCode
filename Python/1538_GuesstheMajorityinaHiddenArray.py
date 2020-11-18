"""
We have an integer array nums, where all the integers in nums are 0 or 1. You will not be given direct access to the array, instead, you will have an API ArrayReader which have the following functions:

int query(int a, int b, int c, int d): where 0 <= a < b < c < d < ArrayReader.length(). The function returns the distribution of the value of the 4 elements and returns:
4 : if the values of the 4 elements are the same (0 or 1).
2 : if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
0 : if two element have a value equal to 0 and two elements have a value equal to 1.
int length(): Returns the size of the array.
You are allowed to call query() 2 * n times at most where n is equal to ArrayReader.length().

Return any index of the most frequent value in nums, in case of tie, return -1.

Follow up: What is the minimum number of calls needed to find the majority element?

 

Example 1:

Input: nums = [0,0,1,0,1,1,1,1]
Output: 5
Explanation: The following calls to the API
reader.length() // returns 8 because there are 8 elements in the hidden array.
reader.query(0,1,2,3) // returns 2 this is a query that compares the elements nums[0], nums[1], nums[2], nums[3]
// Three elements have a value equal to 0 and one element has value equal to 1 or viceversa.
reader.query(4,5,6,7) // returns 4 because nums[4], nums[5], nums[6], nums[7] have the same value.
we can infer that the most frequent value is found in the last 4 elements.
Index 2, 4, 6, 7 is also a correct answer.
Example 2:

Input: nums = [0,0,1,1,0]
Output: 0
Example 3:

Input: nums = [1,0,1,0,1,0,1,0]
Output: -1
 

Constraints:

5 <= nums.length <= 10^5
0 <= nums[i] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-the-majority-in-a-hidden-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
   # Compares 4 different elements in the array
   # return 4 if the values of the 4 elements are the same (0 or 1).
   # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
   # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
   def query(self, a: int, b: int, c: int, d: int) -> int:

   # Returns the length of the array
   def length(self) -> int:


class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        def cmp(q1, q2):
            print(q1, q2)
            tmp1 = reader.query(*q1)
            tmp2 = reader.query(*q2)
            return tmp1 == tmp2

        length = reader.length()
        q0234 = reader.query(0,2,3,4)
        q1234 = reader.query(1,2,3,4)
        q0134 = reader.query(0,1,3,4)
        if q0234 == q1234:
            p, q, z = 0, 1, 2
        elif q0234 == q0134:
            p, q, z = 1, 2, 0
        else:
            p, q, z = 0, 2, 1

        print(q0234, q1234, q0134)
        zeros, ones = 2, 0
        if cmp((p, q, 3, 4),tuple(sorted([z, q, 3, 4]))): # a, b, c, d have to be sorted
            zeros += 1
        else:
            ones += 1
        index = 3
        res = None
        while index + 1 < length:
            tmp = reader.query(p, q, index, index+1)
            if tmp == 4:
                zeros += 2
            elif tmp == 0:
                ones += 2
                res = index
            index += 2
        if index < length:
            if cmp((p, 2, 3, 4), (2, 3, 4, index)):
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            return p
        elif zeros < ones:
            return res
        else:
            return -1


# https://leetcode-cn.com/problems/guess-the-majority-in-a-hidden-array/solution/san-chong-fang-fa-you-yi-dao-nan-by-zerotrac2/
# 作者：zerotrac2
# 链接：https://leetcode-cn.com/problems/guess-the-majority-in-a-hidden-array/solution/san-chong-fang-fa-you-yi-dao-nan-by-zerotrac2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 方法一：暴力使用 API
# 给定的 API 最简单的一种使用方法是：

# 我们可以使用两次 API 得到任意两个位置的数是否相等。具体地，如果我们希望得到位置 p 和 q 的数是否相等，我们只要查询 p, x, y, z 和 q, x, y, z，这两次查询结果相等当且仅当位置 p 和 q 的数相等，其中 x, y, z 是不等于 p, q 的任意三个位置。

# 因此我们可以固定位置 p = 0，然后使用 2(n - 1) 次查询分别得到位置 q = 1, 2, 3, ..., n - 1 和位置 p 的数是否相等。这样我们就还原出了整个数组。


"""
C++

class Solution {
public:
    int guessMajority(ArrayReader &reader) {
        int n = reader.length();
        vector<int> v(n);
        v[0] = 1;

        auto checkIfSame = [&](int p, int q) {
            vector<int> chooseP = {p};
            vector<int> chooseQ = {q};
            for (int i = 0; i < n; ++i) {
                if (i != p && i != q) {
                    chooseP.push_back(i);
                    chooseQ.push_back(i);
                    if (chooseP.size() == 4) {
                        break;
                    }
                }
            }
            sort(chooseP.begin(), chooseP.end());
            sort(chooseQ.begin(), chooseQ.end());
            return reader.query(chooseP[0], chooseP[1], chooseP[2], chooseP[3]) == \
                   reader.query(chooseQ[0], chooseQ[1], chooseQ[2], chooseQ[3]);
        };

        auto find = [&](int num) {
            int idx = -1;
            for (int i = 0; i < n; ++i) {
                if (v[i] == num) {
                    idx = i;
                    break;
                }
            }
            return idx;
        };

        for (int i = 1; i < n; ++i) {
            v[i] = checkIfSame(0, i);
        }
        
        int sum = accumulate(v.begin(), v.end(), 0);
        if (sum * 2 == n) {
            return -1;
        }
        return sum * 2 < n ? find(0) : find(1);
    }
};
方法二：有技巧地使用 API
我们可以发现，如果得到了位置 0, 1, 2, 3, 4 的数，接下来要想得到位置 i (i > 4) 的数，我们只要查询 i - 4, i - 3, i - 2, i - 1 以及 i - 3, i - 2, i - 1, i 即可得到位置 i 和位置 i - 3 的数是否相等。由于位置 i - 3 的数已知，并且相邻两个位置的查询是共用的。而位置 0, 1, 2, 3, 4 的数也可以通过一些技巧快速得到，总共只需要 n + 1 次查询，可以参考下面的代码。



C++

class Solution {
public:
    int guessMajority(ArrayReader &reader) {
        int n = reader.length();
        vector<int> v(n);
        v[0] = 1;

        auto find = [&](int num) {
            int idx = -1;
            for (int i = 0; i < n; ++i) {
                if (v[i] == num) {
                    idx = i;
                    break;
                }
            }
            return idx;
        };

        int q0123 = reader.query(0, 1, 2, 3);
        int q0124 = reader.query(0, 1, 2, 4);
        int q0134 = reader.query(0, 1, 3, 4);
        int q0234 = reader.query(0, 2, 3, 4);
        int q1234 = reader.query(1, 2, 3, 4);
        v[1] = (q0234 == q1234);
        v[2] = (q0134 == q1234);
        v[3] = (q0124 == q1234);
        v[4] = (q0123 == q1234);

        int prev = q1234;
        for (int i = 5; i < n; ++i) {
            int curr = reader.query(i - 3, i - 2, i - 1, i);
            v[i] = (prev == curr ? v[i - 4] : 1 - v[i - 4]);
            prev = curr;
        }

        int sum = accumulate(v.begin(), v.end(), 0);
        if (sum * 2 == n) {
            return -1;
        }
        return sum * 2 < n ? find(0) : find(1);
    }
};
方法三：只查询必要的信息
实际上我们并没有必要复原整个数组，如果我们知道位置 p 和 q 的数相等（假设均为 1），那么我们可以一次性查询两个新的数 x, y：

如果查询结果为 0，说明 x, y 均为 0；
如果查询结果为 2，说明 x, y 其中一个为 0，另一个为 1；
如果查询结果为 4，说明 x, y 均为 1。
这样我们虽然不能复原数组，但仍然可以求出数组中 0 和 1 的个数。如果最后还剩一个数，那么额外加两次查询判断其与位置 0 的数是否相等即可。

那么如何找出 p 和 q 呢？根据鸽巢原理，前三个数中一定有两个数是相等的，因此我们可以使用之前判断两个数是否相等的方法找出 p 和 q。

具体见下面的代码。总查询次数约为 n/2。



C++

class Solution {
public:
    int guessMajority(ArrayReader &reader) {
        // nums[0] = 0
        int cnt0 = 1, cnt1 = 0;
        int q0234 = reader.query(0, 2, 3, 4);
        int q1234 = reader.query(1, 2, 3, 4);
        // 从 start 开始每两个数一查
        int start, p, q;
        // 记录任意一个 0/1 的位置
        int where0 = -1, where1 = -1;
        if (q0234 == q1234) {
            // nums[1] = 0
            ++cnt0;
            start = 2;
            p = 0;
            q = 1;
            where0 = 0;
        }
        else {
            // nums[1] = 1
            ++cnt1;
            int q0134 = reader.query(0, 1, 3, 4);
            if (q0134 == q1234) {
                // nums[2] = 0
                ++cnt0;
                start = 3;
                p = 0;
                q = 2;
                where0 = 0;
                where1 = 1;
            }

"""