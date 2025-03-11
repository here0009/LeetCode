/*
 You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
Example 2:

Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
 

Constraints:

3 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
 */

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        int n = nums.size();
        vector<int> state(n);
        int pre_max = nums[0];
        for (int i = 0; i < n; i++){
            if (nums[i] > pre_max){
                pre_max = nums[i];
                state[i] = 1;
            }
        }
        int res = 0;
        int suffix_min = nums[n-1];
        for (int j = n - 2; j >= 1; j--){
            if (state[j] == 1 && nums[j] < suffix_min){
                res += 2;
            }
            else if (nums[j] < nums[j+1] && nums[j] > nums[j-1]){
                res += 1;
            }
            suffix_min = min(suffix_min, nums[j]);
        }
        return res;
    }
};

int main(){
    Solution s;
    vector<int> nums = {1,2,3};
    cout << s.sumOfBeauties(nums) << endl;
    nums = {2,4,6,4};
    cout << s.sumOfBeauties(nums) << endl;
    nums = {3,2,1};
    cout << s.sumOfBeauties(nums) << endl;
    return 0;
};