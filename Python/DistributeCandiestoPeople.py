"""
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
"""
class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        res = []
        run_sum = (num_people+1)*num_people / 2
        runs = 0  #candies >=(run_sum + run_sum + runs*n**2) * runs /2
        sum_c = run_sum
        while sum_c < candies:
            sum_c += num_people ** 2 + run_sum
            runs += 1

        first = 1 + runs * num_people
        print(run_sum, runs, first)
        index  = 0
        while candies > 0:
            res.append(first)
            candies -= first
            first += 1
            index += 1
        return res


class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        res = [0]*num_people
        index = 0
        tmp = 1
        while candies > 0:
            # print(candies)
            res[index%num_people] += min(candies,tmp)
            candies -= tmp
            tmp += 1
            index += 1
        return res

from math import sqrt
class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        """
        n = num_people
        res[i] equals to sum of [i,i+n,i+2n,...i+kn] untill the sum of res equals to candies, so we can calculate i+kn first, then add the remaing to res.
        m = i + kn, sum of 1 to m is (1+m)*m//2, it must be <= candies, m is int(sqrt(2*candies))
        the index of m is m % num_people -1, the res[index] = (m+index)*((m-index)//n+1)//2
        """
        res = [0]*num_people
        #candies >= (1+m)*m/2
        m = int((-1+sqrt(1+8*candies))/2)
        rounds = m//num_people
        for i in range(num_people):
            res[i] = (i+1+(rounds-1)*num_people+i+1)*rounds//2
        candies -= sum(res)
        # print(m,candies,rounds,res)
        index = 0
        curr = rounds*num_people + 1
        while candies > 0:
            # print(res)
            res[index] += min(candies, curr)
            candies -= curr
            index += 1
            curr += 1     
        return res



s  = Solution()
candies = 7
num_people = 4
# print(s.distributeCandies(15,4))
print(s.distributeCandies(candies, num_people))

candies = 10
num_people = 3
print(s.distributeCandies(candies, num_people))