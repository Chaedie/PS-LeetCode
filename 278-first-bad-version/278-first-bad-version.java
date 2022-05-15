/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        int mid = ((right - left)  / 2) + left;
        
        for (int i = 0; i < n; i++) {
            if (!isBadVersion(mid)) {
                left = mid + 1;
                mid = ((right - left)  / 2) + left;
                continue;
            } else {
                if(mid == 1) {
                    return mid;
                }
                if(!isBadVersion(mid - 1)) {
                    return mid;                    
                } 
                if(isBadVersion(mid-1)) {
                    right = mid - 1;
                    mid = ((right - left)  / 2) + left;
                    continue;
                }                
            }
        }
        return -1;
    }
}