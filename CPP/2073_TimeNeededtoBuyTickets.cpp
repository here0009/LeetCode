#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int n = tickets.size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (i <= k) {
                res += min(tickets[i], tickets[k]);
            } else {
                res += min(tickets[i], tickets[k] - 1);
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> tickets = {5, 1, 1, 1};
    int k = 0;
    int res = s.timeRequiredToBuy(tickets, k);
    cout << res << endl; // Output: 8
    tickets = {2, 3, 2};
    k = 2;
    res = s.timeRequiredToBuy(tickets, k);
    cout << res << endl; // Output: 6
    return 0;
}