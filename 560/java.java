class Solution {
    public int subarraySum(int[] nums, int k) {
        int total = 0;
        int n = nums.length;
        //System.out.println(n);
        HashMap<Integer,Integer> map = new HashMap<>();
        int result = 0; 
        map.put(0,1);
        for(int i = 0 ; i < n; i += 1){
            total = total + nums[i];

            if (map.containsKey(total - k )){
                result = result + map.get(total-k);


            }
            if (!map.containsKey(total)){
                map.put(total,1);
            }
            else{
                map.put(total,map.get(total)+1);

            }
       


        }
        return result;
        
    }
}