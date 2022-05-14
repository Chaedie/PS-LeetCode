class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        int left = 0;
        int right = n - 1;

        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] * nums[i];
        }

        for (int i = 0; i < n; i++) {
            if (nums[left] > nums[right]) {
                result[(n - 1) - i] = nums[left];
                left++;
            } else {
                result[(n - 1) - i] = nums[right];
                right--;
            }
        }
        return result;
    }
}