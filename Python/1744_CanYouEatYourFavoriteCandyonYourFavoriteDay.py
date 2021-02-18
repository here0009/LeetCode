"""
You are given a (0-indexed) array of positive integers candiesCount where candiesCount[i] represents the number of candies of the ith type you have. You are also given a 2D array queries where queries[i] = [favoriteTypei, favoriteDayi, dailyCapi].

You play a game with the following rules:

You start eating candies on day 0.
You cannot eat any candy of type i unless you have eaten all candies of type i - 1.
You must eat at least one candy per day until you have eaten all the candies.
Construct a boolean array answer such that answer.length == queries.length and answer[i] is True if you can eat a candy of type favoriteTypei on day favoriteDayi without eating more than dailyCapi candies on any day, and False otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.

Return the constructed array answer.

 

Example 1:

Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
Output: [True,False,True]
Explanation:
1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
2- You can eat at most 4 candies each day.
   If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
   On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.
Example 2:

Input: candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
Output: [False,True,True,False,False]
 

Constraints:

1 <= candiesCount.length <= 105
1 <= candiesCount[i] <= 105
1 <= queries.length <= 105
queries[i].length == 3
0 <= favoriteTypei < candiesCount.length
0 <= favoriteDayi <= 109
1 <= dailyCapi <= 109
"""


from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        preSum = [0]
        for c in candiesCount:
            preSum.append(preSum[-1] + c)
        res = []
        for f_type, f_day, candi_per_day in queries:
            min_candi = preSum[f_type]
            max_candi = preSum[f_type + 1]
            f_day += 1  # 0 indexed
            if f_day * 1 > max_candi:
                res.append(False)
            elif f_day * candi_per_day <= min_candi:
                res.append(False)
            else:
                res.append(True)
        # print(preSum)
        return res

S = Solution()
if f_type == 43:
    print(f_type, f_day, min_candi, max_candi, f_day*candi_per_day)

candiesCount = [7,4,5,3,8]
queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
print(S.canEat(candiesCount, queries))
candiesCount = [5,2,6,4,1]
queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
print(S.canEat(candiesCount, queries))

candiesCount = [16,38,8,41,30,31,14,45,3,2,24,23,38,30,31,17,35,4,9,42,28,18,37,18,14,46,11,13,19,3,5,39,24,48,20,29,4,19,36,11,28,49,38,16,23,24,4,22,29,35,45,38,37,40,2,37,8,41,33,8,40,27,13,4,33,5,8,14,19,35,31,8,8]
queries = [[35,669,5],[72,822,74],[47,933,94],[62,942,85],[42,596,11],[56,1066,18],[54,571,45],[39,890,100],[3,175,26],[48,1489,37],[40,447,52],[30,584,7],[26,1486,38],[21,1142,21],[9,494,96],[56,759,81],[13,319,16],[20,1406,57],[11,1092,19],[24,670,67],[38,1702,33],[5,676,32],[50,1386,77],[36,1551,87],[29,1445,13],[58,977,13],[7,887,64],[37,1396,23],[0,765,69],[40,1083,86],[43,1054,49],[48,690,92],[28,1201,56],[47,948,43],[57,233,25],[32,1293,65],[0,1646,34],[43,1467,39],[39,484,23],[21,1576,69],[12,1222,68],[9,457,83],[32,65,9],[10,1424,42],[35,534,3],[23,83,22],[33,501,33],[25,679,51],[2,321,42],[1,240,68],[7,1297,42],[45,480,72],[26,1472,9],[6,649,90],[26,361,57],[49,1592,7],[11,158,95],[35,448,24],[41,1654,10],[61,510,43],[31,1230,95],[11,1471,12],[37,43,84],[56,1147,48],[69,1368,65],[22,170,24],[56,192,80],[34,1207,69],[1,1226,22],[37,1633,50],[11,98,58],[17,125,13],[0,1490,5],[37,1732,43],[45,793,14],[16,578,72],[50,241,78]]

Output = [True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True]
Expected = [True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True]
print(S.canEat(candiesCount, queries))

for z, o, e in zip(queries, Output, Expected):
    if o != e:
        print(z, o, e)

