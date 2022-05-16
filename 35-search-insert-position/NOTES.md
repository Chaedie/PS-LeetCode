
- 아래는 디스커스에서 따온 솔루션
  아래 코드의 특징을 보면, 

1. 마지막 숫자가 타겟보다 작으면 바로 "엔드 + 1" 로 리턴하면서 엔드 케이스를 처리했다.
2. for문이 아닌 while문으로 했고,
3. mid == 0 인 케이스도 그냥 if로 안넣고 간단하게 마지막에 return start; 하는 것으로 끝냈다.

부족함을 많이 느낀다.

히든케이스 처리를 어떻게 할지 잘 고민해야한다.
아직 히든케이스 처리에 대한 방법이 잘 떠오르지 않는다.

  
```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1 ;
        if(nums[end] < target ){
            return end + 1;  // to take care of the edge cases
        }
        while(start <= end){
            int mid = start + (end - start)/2 ;
            if(nums[mid]< target){
                start = mid + 1;
            }
            else if (nums[mid]> target){
                end = mid - 1;
            }
            else{
                return mid ;
            }
        }
        return start;
    }
}
```
