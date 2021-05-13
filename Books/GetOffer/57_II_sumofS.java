/*
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
public class MainClass {
    public static String int2dArrayToString(int[][] array) {
        if (array == null) {
            return "null";
        }
        if (array.length == 0) {
            return "[]";
        }
    
        StringBuilder sb = new StringBuilder("[");
        for (int[] item : array) {
            sb.append("[");
            for (int letter: item){
                sb.append(Integer.toString(letter));
                sb.append(",");
            }
            sb.setCharAt(sb.length() - 1, ']');
        }
        sb.append("]");
        return sb.toString();
    }
    
    public static void main(String[] args) throws IOException {

        int target = 25;
        
        int[][] ret = new Solution().findContinuousSequence(target);
        
        String out = int2dArrayToString(ret);
        
        System.out.print(out);

    }
}

// https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
class Solution {
    public int[][] findContinuousSequence(int target) {
        int i = 1;
        int j = 1;
        int sum = 0;
        List<int []> res = new ArrayList<>();
        while (i <= target / 2){
            if (sum < target){
                sum += j;
                j += 1;
            }
            else if (sum > target){
                sum -= i;
                i += 1;
            }
            else{
                int [] arr = new int[j - i];
                for (int k = i; k < j; k ++){
                    arr[k - i] = k;
                }
                res.add(arr);
                sum -= i;
                i += 1;
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}
