import java.io.IOException;



public class MainClass {
    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return new int[0];
        }

        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static void main(String[] args) throws IOException {

        String line = "[5,7,7,8,8,10]";

        int[] nums = stringToIntegerArray(line);

        int target = 8;

        int ret = new Solution().search(nums, target);

        String out = String.valueOf(ret);

        System.out.print(out);

    }
}


public class Solution {
    public int search(int[] nums, int target) {

        if (nums.length == 0) return 0;
        int left = 0;
        int right = nums.length - 1;
        while ( left < right){
            int mid  = (left + right) / 2;
            if (nums[mid] < target){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }
        // return left;
        int left2 = 0;
        int right2 = nums.length - 1;
        while (left2 < right2) {
            int mid2 = (left2 + right2) / 2;
            if (nums[mid2] > target) {
                right2 = mid2;
            } else {
                left2 = mid2 + 1;
            }
        }
        System.out.println(left);
        System.out.println(left2);
        if (nums[left2] == target){
            return left2 - left + 1;
        }
        return left2 - left;

    }
}