class Solution {
    int row;
    int col;
    String w;
    public boolean exist(char[][] board, String word) {
        row = board.length;
        col = board[0].length;
        w = word;
        boolean [][] visited = new boolean [row][col];
        for (int i = 0; i < row; i++){
            for (int j = 0; j < col; j++){
                if (dfs(board, 0, i, j)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, int idx, int i, int j){
        if (! inRange(i, j) || w.charAt(idx) != board[i][j]) return false;
        if (idx == w.length() - 1) return true;
        board[i][j] = '\0';
        boolean res = dfs(board, idx + 1, i - 1, j) || dfs(board, idx + 1, i + 1, j) || dfs(board, idx + 1, i, j - 1) || dfs(board, idx + 1, i, j + 1) ;
        board[i][j] = w.charAt(idx);
        return res;
    }


    private boolean inRange(int i, int j){
        return i >=0 && i < row && j >=0 && j < col;
    }
}