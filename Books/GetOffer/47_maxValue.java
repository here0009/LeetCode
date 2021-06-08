

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

    public static void main(String[] args) throws IOException {

        String line;

        int[][] grid = stringToInt2dArray(line);

        int ret = new Solution().maxValue(grid);

        String out = String.valueOf(ret);

        System.out.print(out);
    }
}

class Solution {
    public int maxValue(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int matrix[][] = new int[row + 1][col + 1];
        for (int i = 1; i < row + 1; i++){
            for (int j = 1; j < col + 1; j++){
                matrix[i][j] = Math.max(matrix[i - 1][j], matrix[i][j - 1]) + grid[i - 1][j - 1];
            }
        }
        return matrix[row][col];
    }
}