/*
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
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
  int digit_sum(int num) {
    int res = 0;
    while (num > 0) {
      res += num % 10;
      num = num / 10;
    }
    return res;
  }

  int countLargestGroup(int n) {
    unordered_map<int, int> counts;
    for (int i = 1; i < n + 1; i++) {
      counts[digit_sum(i)] += 1;
    }
  auto max_iter = max_element(counts.begin(), counts.end(), [](const auto& p1, const auto& p2) {
        return p1.second < p2.second;
    });
  int res = 0;
  for (const auto& pair : counts) {
    if (pair.second == max_iter->second) {
      res++;
    }
  }
  return res;
  }
};

int main() {
  Solution sol;
  cout << sol.countLargestGroup(13) << endl;
  cout << sol.countLargestGroup(2) << endl;
  cout << sol.countLargestGroup(46) << endl;
}
