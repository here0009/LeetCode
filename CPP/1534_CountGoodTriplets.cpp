/*
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
 

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
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
  int countGoodTriplets(const vector<int>& arr, int a, int b, int c) {
    int res = 0, n = arr.size();
    for (int i = 0; i < n - 2; i++) {
      for (int j = i + 1; j < n - 1; j++) {
        if (abs(arr[i] - arr[j]) <= a) {
          for (int k = j + 1; k < n; k++) {
            if (abs(arr[i] - arr[k]) <=c && abs(arr[j] - arr[k]) <=b) {
              res += 1;
            }
          }
        }
      }
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<int> arr = {3, 0, 1, 1, 9, 7};
  int a = 7, b = 2, c = 3;
  cout << s.countGoodTriplets(arr, a, b, c) << endl;   // Output: 4
  // Example 2
  arr = {1, 1, 2, 2, 3};
  a = 0, b = 0, c = 1;
  cout << s.countGoodTriplets(arr, a, b, c) << endl;   // Output: 0
  // Example 3
  arr = {1, 2, 3, 4, 5};
  a = 1, b = 1, c = 1;
  cout << s.countGoodTriplets(arr, a, b, c) << endl;   // Output: 0
  return 0;
}