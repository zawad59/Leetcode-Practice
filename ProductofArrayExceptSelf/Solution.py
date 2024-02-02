class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    std::vector<int> leftProduct(n, 1);
    std::vector<int> rightProduct(n, 0);
    std::vector<int> outputArr(n, 0);

    rightProduct[n - 1] = 1;

    int i = 1;
    int j = n - 2;

    while (i != n) {
        leftProduct[i] = nums[i - 1] * leftProduct[i - 1];
        i++;
    }

    while (j >= 0) {
        rightProduct[j] = nums[j + 1] * rightProduct[j + 1];
        j--;
    }

    for (int k = 0; k < n; k++) {
        outputArr[k] = leftProduct[k] * rightProduct[k];
    }

    return outputArr;
    }
};