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

    public static String integerArrayToString(int[] nums, int length) {
        if (length == 0) {
            return "[]";
        }

        String result = "";
        for (int index = 0; index < length; index++) {
            int number = nums[index];
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayToString(int[] nums) {
        return integerArrayToString(nums, nums.length);
    }

    public static void main(String[] args) throws IOException {
        
        String line = "[1,2,3,4]";

        int[] nums = stringToIntegerArray(line);

        int[] ret = new Solution().exchange(nums);

        String out = integerArrayToString(ret);

        System.out.print(out);

    }
}


// class Solution {
//     public int[] exchange(int[] nums) {
//         int left = 0;
//         int length = nums.length;
//         int right = length - 1;
//         while ( left < right){
//             while ( left < length && nums[left] % 2 == 1){
//                 left += 1;
//             }
//             while ( right > 0 && nums[right] % 2 == 0){
//                 right -= 1;
//             }
//             if (left < right && left < length && right > 0){
//                 int tmp = nums[left];
//                 nums[left] = nums[right];
//                 nums[right] = tmp;
//                 left += 1;
//                 right -= 1;
//             }
//         }
//         return nums;

//     }
// }

class Solution {
    public int[] exchange(int[] nums) {
        int i = 0, j = nums.length - 1, tmp;
        while(i < j) {
            while(i < j && (nums[i] & 1) == 1) i++;
            while(i < j && (nums[j] & 1) == 0) j--;
            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        return nums;
    }
}

// 作者：jyd 链接：https:// leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/mian-shi-ti-21-diao-zheng-shu-zu-shun-xu-shi-qi-4/
// 来源：力扣（LeetCode）著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
