/*
 */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
 public:
  int countCompleteSubarrays(const vector<int>& nums) {
    unordered_map<int, int> counter;
    int left = 0, right = 0, res = 0;
    unordered_set<int> num_set(nums.begin(), nums.end());
    int target_num = num_set.size();
    while (right < nums.size()) {
      counter[nums[right]] += 1;
      if (counter.size() == target_num) {
        while (left < right && counter[nums[left]] > 1) {
          counter[nums[left]] -= 1;
          left += 1;
        }
        res += left + 1;
      }
      right++;
    }
    return res;
  }
};

int main() {
  Solution sol;
  vector<int> nums = {1, 3, 1, 2, 2};
  cout << sol.countCompleteSubarrays(nums) << endl;
  nums = {5, 5, 5, 5};
  cout << sol.countCompleteSubarrays(nums) << endl;
}
