import java.io.IOException;
import java.lang.Math;

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

    public static int[][] stringToInt2dArray(String input) {
        JsonArray jsonArray = JsonArray.readFrom(input);
        if (jsonArray.size() == 0) {
            return new int[0][0];
        }

        int[][] arr = new int[jsonArray.size()][];
        for (int i = 0; i < arr.length; i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            arr[i] = stringToIntegerArray(cols.toString());
        }
        return arr;
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

        String line = "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]";

        int[][] matrix = stringToInt2dArray(line);

        int[] ret = new Solution().spiralOrder(matrix);

        String out = integerArrayToString(ret);

        System.out.print(out);

    }
}


class Solution {
    public int[] spiralOrder(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int layer = 0;
        int k = 0;
        int max_layer = Math.min(row, col) / 2;
        if (Math.min(row, col) % 2 == 1) max_layer++;
        int [] res = new int[row * col];
        System.out.println(max_layer);
        while (layer < max_layer){
            for (int j = layer; j < col - layer - 1; j++) res[k++] = matrix[layer][j];
            for (int i = layer; i < row - layer - 1; i++) res[k++] = matrix[i][col - layer - 1];
            for (int j = col - layer - 1; j > layer; j--) res[k++] = matrix[row - layer - 1][j];
            for (int i = row - layer - 1; i > layer; i--) res[k++] = matrix[i][layer];
            layer += 1;
        }
        if (k < row * col) res[k++] = matrix[layer][layer];
        return res;
    }
}

class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if (matrix.length == 0) {
            return new int[0];
        }
        int left = 0;
        int up = 0;
        int k = 0;
        int down = matrix.length - 1;
        int right = matrix[0].length - 1;
        int[] res = new int[(down + 1)*(right + 1)];
        while (left < right && up < down){
            for (int j = left; j < right; j++) res[k++] = matrix[up][j];
            for (int i = up; i < down; i++) res[k++] = matrix[i][right];
            for (int j = right; j > left; j--) res[k++] = matrix[down][j];
            for (int i = down; i > up; i--) res[k++] = matrix[i][left];
            left += 1;
            right -= 1;
            up += 1;
            down -= 1;
        }
        if (left == right && up == down)
        {
            res[k++] = matrix[left][up];
        }
        else if  (left < right && up == down){
            for (int j = left; j <= right; j++) res[k++] = matrix[up][j];
        }
        else if (left == right && up < down) {
            for (int i = up; i <= down; i++) res[k++] = matrix[i][right];
        }
        return res;
    }
}

// System.out.println(k);
// System.out.println(left);
// System.out.println(right);
// System.out.println(up);
// System.out.println(down);