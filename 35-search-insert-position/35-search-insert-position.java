class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;
        int mid = ((right - left) / 2) + left;

        for (int i = 0; i < n; i++) {
            // if(n == 1) == if(mid == n-1)
            // if (n == 1) {
            //     if (nums[mid] < target){
            //         return 1;
            //     }
            //     return 0;
            // }
            // mid == n - 1;
            if (nums[mid] == target) {
                return mid;
            }
            // n == 1, mid == n-1
            if (mid == n - 1) {
                if (nums[mid] < target) {
                    return n;
                }
                return n - 1;
            }
            // mid == 0
//            if (mid == 0) {
//                if (nums[mid] < target) {
//                    return mid + 1;
//                }
//                return mid;
//            }
            // 0 <= mid < n - 1
            if (mid >= 0 && mid < n - 1) {

                if (nums[mid] < target) {
                    if (nums[mid + 1] > target) {
                        return mid + 1;
                    }
                    left = mid + 1;
                    mid = ((right - left) / 2) + left;
                    continue;
                }
                if (nums[mid] > target) {
                    if (mid == 0) {
                        return mid;
                    }
                    if (nums[mid - 1] < target) {
                        return mid;
                    }
                    right = mid - 1;
                    mid = ((right - left) / 2) + left;
                    continue;
                }
            }
        }
        return -1;
    }
}