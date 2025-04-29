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
  int64_t countInterestingSubarrays(const vector<int>& nums, int modulo, int k) {
    int presum = 0;
    int64_t res = 0;
    vector<int> counts(min(static_cast<int>(nums.size() + 1), modulo));
    counts[0] = 1;
    for (auto num : nums) {
      presum += num % modulo == k;
      if (presum >= k) {
        res += counts[(presum - k) % modulo];
      }
      counts[presum % modulo]++;
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<int> nums = {3, 2, 4};
  int modulo = 2;
  int k = 1;
  cout << s.countInterestingSubarrays(nums, modulo, k) << endl;   // Output: 3
  nums = {3, 1, 9, 6};
  modulo = 3;
  k = 0;
  cout << s.countInterestingSubarrays(nums, modulo, k) << endl;   // Output: 2
  return 0;
}