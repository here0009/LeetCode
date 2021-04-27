class Solution {

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 2, 2, 2, 5, 4, 2};
        System.out.println(majorityElement(nums));
        int[] nums2 = {5, 5, 5, 3, 2};
        System.out.println(majorityElement(nums2));        
    }

    public static int majorityElement(int[] nums) {
        int counts = 1;
        int res = nums[0];
        for (int num : nums) {
            if (num == res) {
                counts += 1;
            } else {
                counts -= 1;
            }    
            if (counts == 0){
                res = num;
                counts = 1;
            }
        }
        return res;
    }
}