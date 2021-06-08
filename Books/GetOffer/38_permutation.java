import java.util.HashSet;
import java.util.Set;

class Solution {
    public String[] permutation(String s) {
        Set<String> res = new HashSet<>();
        boolean [] visited = new boolean[s.length()];
        backtrack(s.toCharArray() , "", visited, res);
        return res.toArray(new String[res.size()]);
    }
    private void backtrack(char[] chars, String tmp, boolean [] visited, Set<String> res){
        if (tmp.length() == chars.length){
            res.add(tmp);
            return;
        }
        for (int i = 0; i < chars.length; i++){
            if (! visited[i]){
                visited[i] = true;
                backtrack(chars, tmp + chars[i], visited, res);
                visited[i] = false;
            }
        }
    }
}



class Solution {

    char [] chars;
    Set<String> res = new HashSet<>();
    public String[] permutation(String s) {
        chars = s.toCharArray();
        boolean [] visited = new boolean[s.length()];
        backtrack("", 0, visited);
        return res.toArray(new String[res.size()]);
    }

    private void backtrack(String tmp, int idx, boolean [] visited) {
        if (idx == chars.length) {
            res.add(tmp);
            return;
        }
        for (int i = 0; i < chars.length; i++) {
            if (visited[i] == false) {
                visited[i] = true;
                backtrack(tmp + chars[i], idx + 1, visited);
                visited[i] = false;
            }
        }
    }
}