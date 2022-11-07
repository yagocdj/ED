#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum_right {0}, sum_left {0};
        for (int i = 0; i < nums.size(); i++) {
            sum_left = 0;
            sum_right = 0;
            for (int j = i+1; j < nums.size()-1; j++) {
                sum_left += nums[j];
            }
            for (int k = i-1; k > 0; k--) {
                sum_right += nums[k];
            }
            if (sum_left == sum_right) {
                return i;
            }
        }
        return -1;
    }
};

int main(void) {

    Solution sol;
    vector<int> nums = {1,7,3,6,5,6};;

    int result = sol.pivotIndex(nums);

    cout << result << endl;

    return 0;
}