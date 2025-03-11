// You are given m arrays, where each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|. Your task is to find the maximum distance.

//  

// Example 1:

// Input: arrays = [[1,2,3],[4,5],[1,2,3]]
// Output: 4
// Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
// Example 2:

// Input: arrays = [[1],[1]]
// Output: 0
// Example 3:

// Input: arrays = [[1],[2]]
// Output: 1
// Example 4:

// Input: arrays = [[1,4],[0,5]]
// Output: 4
//  

// Constraints:

// m == arrays.length
// 2 <= m <= 104
// 1 <= arrays[i].length <= 500
// -104 <= arrays[i][j] <= 104
// arrays[i] is sorted in ascending order.
// There will be at most 105 integers in all the arrays.
// g++ -o max_distance 624_MaximumDistanceinArrays.cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;


class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int t_max = INT_MIN / 2,  t_min = INT_MAX / 2;
        int res = 0;
        
        for (auto lst : arrays) {
            res = max(res, max(t_max - lst.front(), lst.back() - t_min));
            t_max = max(t_max, lst.back());
            t_min = min(t_min, lst.front());
        }
        return res;
    }
};

int main(){
    Solution s;
    vector<vector<int>> arrays = {{1, 2, 3}, {4, 5}, {1, 2, 3}};
    cout << s.maxDistance(arrays) << endl;
    return 0;
}
