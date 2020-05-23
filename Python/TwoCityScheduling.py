"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""
class Solution_2:
    def twoCitySchedCost(self, costs) -> int:
        print(len(costs))
        N = len(costs)//2
        diff_cost_dict = {}
        for i in range(2*N):
            cost = costs[i]
            diff_cost_dict[cost[0]-cost[1]] = i
        res = 0
        print(len(diff_cost_dict))
        print(diff_cost_dict)
        
        diff_cost_list = sorted(diff_cost_dict.keys())
        print(len(diff_cost_list))
        print(diff_cost_list)

        for i in range(len(diff_cost_list)//2):
            print(res)
            res += costs[diff_cost_dict[diff_cost_list[i]]][0]
        for i in range(len(diff_cost_list)//2, len(diff_cost_list)):
            print(res)
            res += costs[diff_cost_dict[diff_cost_list[i]]][1]
        return res



class Solution_1:
    def twoCitySchedCost(self, costs) -> int:

        N = len(costs)//2
        res = 0
        diff_cost_list = [(cost[0] - cost[1]) for cost in costs]
        
        median_diff_cost = sorted(diff_cost_list)[N-1]
        # print(sorted(diff_cost_list)[:N])
        # print(sorted(diff_cost_list)[N:])
        # print(diff_cost_list)
        # print(median_diff_cost)
        counts_left = 0
        median_list = []
        for i in range(2*N):
            if diff_cost_list[i] < median_diff_cost:
                res += costs[i][0]
                counts_left += 1
            elif diff_cost_list[i] > median_diff_cost:
                res += costs[i][1]
            else:
                median_list.append(i)
        for key in median_list:
            if counts_left < N:
                res += costs[key][0]
                counts_left += 1
            else:
                res += costs[key][1]
        return res

class Solution:
    def twoCitySchedCost(self, costs) -> int:
        costs = sorted(costs, key = lambda x: x[0]-x[1])
        res  =0
        for i in range(len(costs)//2):
            res += costs[i][0]
        for i in range(len(costs)//2, len(costs)):
            res += costs[i][1]
        # print(costs)
        return res

s = Solution()
s_1 = Solution_1()
# costs = [[10,20],[30,200],[400,50],[30,20]]
# print(s.twoCitySchedCost(costs))

# costs = [[10,20],[30,200]]
# print(s.twoCitySchedCost(costs))

# costs = [[945,563],[598,753],[558,341],[372,54],[39,522],[249,459],[536,264],[491,125],[367,118],[34,665],[472,410],[109,995],[147,436],[814,112],[45,545],[561,308],[491,504],[113,548],[626,104],[556,206],[538,592],[250,460],[718,134],[809,221],[893,641],[404,964],[980,751],[111,935]]
# print(s.twoCitySchedCost(costs))


costs = [[33,135],[849,791],[422,469],[310,92],[253,489],[995,760],[852,197],[658,216],[679,945],[197,341],[362,648],[22,324],[408,25],[505,734],[463,279],[885,512],[922,850],[784,500],[557,860],[528,367],[877,741],[554,545],[598,888],[558,104],[426,427],[449,189],[113,51],[201,221],[251,62],[981,897],[392,519],[115,70],[961,109],[512,678],[476,708],[28,902],[763,282],[787,774],[925,475],[253,532],[100,502],[110,857],[822,942],[231,186],[869,491],[651,344],[239,806],[651,193],[830,360],[427,69],[776,875],[466,81],[520,959],[798,775],[875,199],[110,396]]
print(s.twoCitySchedCost(costs))
print(s_1.twoCitySchedCost(costs))