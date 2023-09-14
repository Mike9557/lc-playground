class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = new int[]{-1,-1};
        int n = nums.length;
        for(int i = 0 ; i < nums.length;i++){
            if(nums[i] == target){
                //System.out.println(i);
                //System.out.println(nums[i]);
                ans[0] = i;
                break;
            }
            if( (i == n - 1) & (nums[i] != target)){
                return ans;
            }

        }

        for(int i = n -1 ; i > -1; i--){
            if(nums[i] == target){
                ans[1] = i;
                break;
            }
        }
        

        return ans;
        
    }
}