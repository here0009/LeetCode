/*
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

 

Example 1:

Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
Example 2:

Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
 

Constraints:

3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.
 */
#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution_1 {
 public:
  int arithmeticTriplets(const vector<int>& nums, int diff) {
    int res = 0;
    int length = nums.size();
    for (int i = 0; i < length - 2; i++) {
      for (int j = 1; j < length - 1; j++) {
        if (nums[j] - nums[i] != diff) {
          continue;
        }
        for (int k = 1; k < length; k++) {
          if (nums[k] - nums[j] == diff) {
            res += 1;
          }
        }
      }
    }
    return res;
  }
};

class Solution {
 public:
  int arithmeticTriplets(const vector<int>& nums, int diff) {
    unordered_set<int> num_set;
    int res = 0;
    for (int num : nums) {
      num_set.emplace(num);
    }
    for (int num : nums) {
      if (num_set.count(num + diff) && num_set.count(num + 2*diff)) {
        res += 1;
      }
    }
    return res;
  }
};



int main() {
  Solution s;
  vector<int> nums {0, 1, 4, 6, 7, 10};
  cout << s.arithmeticTriplets(nums, 3) << endl;
  vector<int> nums2 {4, 5, 6, 7, 8, 9};
  cout << s.arithmeticTriplets(nums2, 2) << endl;
  return 0;
}