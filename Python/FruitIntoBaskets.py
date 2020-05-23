"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(set(tree)) <= 2:
            return len(tree)
        fruit_set = {tree[0]}
        start = 0
        end = 0
        continous_num = 1 #store the continous_num of a specific fruit
        res = 0

        for i in range(1, len(tree)):
            if tree[i] not in fruit_set:
                fruit_set.add(tree[i])
                if len(fruit_set) > 2: #the third fruit will replace the first one, new session begin
                    end = i
                    fruit_set = {tree[i], tree[i-1]} #update fruit set
                    fruit_num = end - start
                    if fruit_num > res:
                        res = end - start
                    start = end - continous_num #update start num
                continous_num = 1 #update continous_num
            else:
                if tree[i] == tree[i-1]:
                    continous_num += 1
                else:
                    continous_num = 1
                if i == len(tree) - 1: #the end of the tree, but not a new fruit
                    end = i
                    fruit_num = end - start + 1
                    if fruit_num > res:
                        res = fruit_num
        return res

s = Solution()
test = [1,2,1]
print(s.totalFruit(test))
test = [0,1,2,2]
print(s.totalFruit(test))
test = [1,2,3,2,2]
print(s.totalFruit(test))
test = [3,3,3,1,2,1,1,2,3,3,4]
print(s.totalFruit(test))
test = [6,2,1,1,3,6,6]
print(s.totalFruit(test))