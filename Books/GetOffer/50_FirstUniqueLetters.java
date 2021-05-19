import java.util.HashMap;
import java.util.Map;
import java.io.IOException;

public class MainClass {

    public static void main(String[] args) throws IOException {

        String line = "abaccdeff";
        char ret = new Solution().firstUniqChar(line);
        System.out.print(ret);

    }
}


// class Solution {
//     public char firstUniqChar(String s) {
//         Map<Character, Integer> frequency = new HashMap<Character, Integer>();
//         for (int i = 0; i < s.length(); i++){
//             char ch = s.charAt(i);
//             frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
//         }
//         for (int i = 0; i < s.length(); i++){
//             char ch = s.charAt(i);
//             if (frequency.get(ch) == 1){
//                 return ch;
//             } 
//         }
//         return ' ';
//     }
// }


// class Solution {
//     public char firstUniqChar(String s) {
//         HashMap<Character, Boolean> dic = new HashMap<>();
//         char[] sc = s.toCharArray();
//         for(char c : sc)
//             dic.put(c, !dic.containsKey(c));
//         for(char c : sc)
//             if(dic.get(c)) return c;
//         return ' ';
//     }
// }

// 作者：jyd 链接：https:// leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
// 来源：力扣（LeetCode）著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution {
public char firstUniqChar(String s) {if (s == null || s.equals("")) {
            return ' ';
        }
        int[] count = new int[26];
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            int index = chars[i] - 'a';
            count[index]++;
        }
        for (int i = 0; i < chars.length; i++) {
            int index = chars[i] - 'a';
            if (count[index] == 1) {
                return chars[i];
            }
        }
        return ' ';
    }
}