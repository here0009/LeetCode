import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution {
    
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> map = new HashMap<>();
        return dfs(head);
    }
    private Node dfs(Node node, HashMap<Node, Node> map){
        if (node == null) return null;
        if (map.containsKey(node)) return map.get(node);
        Node node2 = new Node(node.val);
        map.put(node, node2);
        node2.next = dfs(node.next, map);
        node2.random = dfs(node.random, map);
        return node2;
    }
}


class Solution {

    HashMap<Node, Node> map = new HashMap<>();
    public Node copyRandomList(Node head) {

        return dfs(head);
    }

    private Node dfs(Node node) {
        if (node == null)
            return null;
        if (map.containsKey(node))
            return map.get(node);
        Node node2 = new Node(node.val);
        map.put(node, node2);  // set the value before dfs
        node2.next = dfs(node.next);
        node2.random = dfs(node.random);
        return node2;
    }
}