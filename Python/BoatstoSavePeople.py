class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        Thoughts:
        convert people to a dictionary p_weight, key is the weight and value the counts.
        if weight p_weight[limit] = k, then boats += k
        if weight p_weight[limit-1] = j, then boats += j

        calculate from limit-1 to half_limit+1, make complement as possible
        then from 1 to limit//2 boats += sum(p_weight)//2 (+1 if necessary)
        from limit//2 + 1 to limit -1 boats += sum(p_weight) (if there is anything left)
        """
        boats = 0
        p_weight = dict()
        for p in people:
            p_weight[p] = p_weight.get(p, 0) + 1
        
        #print(p_weight)
        half_limit = limit//2
        if limit in p_weight:
            boats += p_weight[limit]
            p_weight[limit] = 0

        complement = 1 #to add with weight, so the total weight <= limit
        for weight in range(limit-1, half_limit, -1):
            if weight in p_weight:
                #print("weight",weight)
                tmp = p_weight[weight]
                while complement < limit - weight + 1:
                    if complement in p_weight:
                        if p_weight[complement] == tmp:
                            boats += tmp
                            p_weight[complement] = 0
                            p_weight[weight] = 0
                            complement += 1
                            break
                        elif p_weight[complement] > tmp:
                            boats += tmp
                            p_weight[complement] -= tmp
                            p_weight[weight] = 0
                
                            break
                        else:
                            tmp -= p_weight[complement]
                            p_weight[weight] -= p_weight[complement]
                            boats += p_weight[complement]
                            p_weight[complement] = 0
                            
                            complement += 1
                    else:
                        complement += 1

        #print("boats",boats)

        for key, value in p_weight.items():
            if key > half_limit:
                #print(key)
                boats += value
            else:
                boats += value/2

        #print("boats",boats)

        boats = int(boats + 0.5) #round up    
        #print(p_weight)       
        return boats

s = Solution()
# p_test = [1,1,1,2,2,3,3,3,3]
# limit_test = 3
## print(s.numRescueBoats(p_test, limit_test))

p_test = [3,2,2,1]
limit_test = 3
print(s.numRescueBoats(p_test, limit_test))

##Another Solution from LeetCode
"""
Sort people, then for each minimum people[l], find the greatest available people[r] so that l, r can use the same boat until l, r meets.
l + r do not have to be limit, it just need to <= limit
USE Greedy Algorithm


class Solution:

    def numRescueBoats(self, people, limit):
        N = len(people)
        people.sort()
        
        l, r = 0, N-1
        
        cnt = 0
        
        while l<=r:
            if people[l]+people[r]<=limit:
                l += 1
                r -= 1
            else:
                r -= 1
            cnt += 1
            
        return cnt
"""