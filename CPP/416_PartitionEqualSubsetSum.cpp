/*
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
 */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
using namespace std;

class Solution {
 public:
  bool canPartition(vector<int>& nums) {
    int sum_val = accumulate(nums.begin(), nums.end(), 0);
    if (sum_val % 2) {
      return false;
    }
    int half_val = sum_val / 2;
    vector<int> dp(half_val + 1);
    dp[0] = true;
    int s2 = 0;
    for (int val : nums) {
      s2 = min(s2 + val, half_val);
      for (int j=s2; j >= val; j--) {
        dp[j] |= dp[j-val];
      }
      cout << " val: " << val << endl;
      cout << "dp: ";
      for (int i = 0; i < dp.size(); i++) {
        cout << dp[i] << " ";
      }
      cout << endl;
      if (dp[half_val]) {
        return true;
      }
    }
    return false;
  }
};

int main() {
  Solution solution;
  vector<int> nums = {1, 5, 11, 5};
  cout << solution.canPartition(nums) << endl;  // Output: true
  nums = {1, 2, 3, 5};
  cout << solution.canPartition(nums) << endl;  // Output: false
  return 0;
}