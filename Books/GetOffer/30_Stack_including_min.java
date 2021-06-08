import java.util.Deque;
import java.util.LinkedList;


class MinStack {

    Deque<Integer> q;
    Deque<Integer> min_q;

    /** initialize your data structure here. */
    public MinStack() {
        q = new LinkedList<Integer>();
        min_q = new LinkedList<Integer>();
    }

    public void push(int x) {
        q.addLast(x);
        if (min_q.isEmpty() || min_q.getLast() >= x) min_q.add(x);
    }

    public void pop() {
        if (q.isEmpty()) return;
        int val = q.pollLast();
        if (! min_q.isEmpty() && min_q.getLast() == val) min_q.pollLast();
    }

    public int top() {
        // if (q.isEmpty()) return;
        return q.getLast();
    }

    public int min() {
        // if (min_q.isEmpty()) return;
        return min_q.getLast();
    }
}

/**
 * Your MinStack object will be instantiated and called as such: MinStack obj =
 * new MinStack(); obj.push(x); obj.pop(); int param_3 = obj.top(); int param_4
 * = obj.min();
 */