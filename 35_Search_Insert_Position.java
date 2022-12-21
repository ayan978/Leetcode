class Solution {
    public int searchInsert(int[] nums, int target) {
        
        boolean b = false;
        
        int low = 0;
        int high = nums.length-1;
        int mid=0;
        while(low<=high){
            mid = (low + high)/2;
            if(target>nums[mid]){
                low = mid+1;
            }
            else if(target<nums[mid]){
                high = mid-1;
            }
            else{
                b = true;
                break;
            }
        }

        int result = b ? mid : low;
        return result;
    }
}
