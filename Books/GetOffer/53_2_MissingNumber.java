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

        String line = "[0,1,2,3,4,5,6,7,9]";

        int[] nums = stringToIntegerArray(line);

        int ret = new Solution().missingNumber(nums);

        String out = String.valueOf(ret);

        System.out.print(out);
    }
}

class Solution {
    public int missingNumber(int[] nums) {
        int left = 0;
        int right = nums.length;
        while (left < right){
            int mid = (left + right) / 2;
            if (nums[mid] == mid){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }
        return left;
    }
}