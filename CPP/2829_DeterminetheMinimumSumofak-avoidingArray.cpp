/*
You are given two integers, n and k.

An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.

Return the minimum possible sum of a k-avoiding array of length n.

 

Example 1:

Input: n = 5, k = 4
Output: 18
Explanation: Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.
Example 2:

Input: n = 2, k = 6
Output: 3
Explanation: We can construct the array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.
 

Constraints:

1 <= n, k <= 50
 */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
using namespace std;

class Solution1 {
 public:
    int minimumSum(int n, int k) {
      vector<int> res {};
      unordered_set<int> avoid {};
      int num = 1;
      while (res.size() < n) {
        if (avoid.count(num) == 0) {
          res.push_back(num);
          avoid.emplace(k - num);
        }
        num += 1;
      }
    return accumulate(res.begin(), res.end(), 0);
    }
};

class Solution {
 public:
    int minimumSum(int n, int k) {
        if (n <= k / 2) {
            return arithmeticSeriesSum(1, 1, n);
        } else {
            return arithmeticSeriesSum(1, 1, k / 2) + arithmeticSeriesSum(k, 1, n - k / 2);
        }
    }

 private:
    int arithmeticSeriesSum(int a1, int d, int n) {
        return (a1 + a1 + (n - 1) * d) * n / 2;
    }
};

int main() {
  Solution s;
  int n = 5, k = 4;
  cout << "res: " << s.minimumSum(n, k) << endl;
  cout <<  "res: " << s.minimumSum(2, 6) << endl;
}