import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;

public class SegmentTree {
    private static int N, O;
    private static int n;
    private static int[] a;
    private static Node[] tree;
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static PrintStream out = new PrintStream(System.out, false);


    // Internal Node class to hold sum and max values
    private static class Node {
        int sum;
        int max;

        Node(int sum, int max) {
            this.sum = sum;
            this.max = max;
        }
    }

    // Function to build the tree
    private static void build(int[] arr) {
        // Insert leaf nodes in the tree
        for (int i = 0; i < n; i++) {
            tree[n + i] = new Node(arr[i], arr[i]);
        }
        // Build the tree by calculating parents
        for (int i = n - 1; i > 0; i--) {
            tree[i] = new Node(
                tree[i << 1].sum + tree[i << 1 | 1].sum,
                Math.max(tree[i << 1].max, tree[i << 1 | 1].max)
            );
        }
    }

    // Function to update a tree node
    private static void updateTreeNode(int p, int value) {
        // Set value at position p
        p = p + n;
        tree[p] = new Node(value, value);

        // Move upward and update parents
        while (p > 1) {
            p >>= 1;
            tree[p] = new Node(
                tree[p << 1].sum + tree[p << 1 | 1].sum,
                Math.max(tree[p << 1].max, tree[p << 1 | 1].max)
            );
        }
    }

    // Function to get sum on interval [l, r)
    private static int sumQuery(int l, int r) {
        int res = 0;
        l += n;
        r += n;

        while (l < r) {
            if ((l & 1) == 1) {
                res += tree[l++].sum;
            }
            if ((r & 1) == 1) {
                res += tree[--r].sum;
            }
            l >>= 1;
            r >>= 1;
        }

        return res;
    }

    // Function to get max on interval [l, r)
    private static int maxQuery(int l, int r) {
        int res = Integer.MIN_VALUE;
        l += n;
        r += n;

        while (l < r) {
            if ((l & 1) == 1) {
                res = Math.max(res, tree[l++].max);
            }
            if ((r & 1) == 1) {
                res = Math.max(res, tree[--r].max);
            }
            l >>= 1;
            r >>= 1;
        }

        return res;
    }

    private static void parser(char ch, int n1, int n2) {
        

        // make a printstream that has autoFlush set to false
        

        switch (ch) {
            case 'M':
                out.println(maxQuery(n1, n2));
                break;
            case 'S':
                out.println(sumQuery(n1, n2));
                break;
            case 'U':
                updateTreeNode(n1, n2);
                break;
        }
    }

    public static void main(String[] args) throws IOException { 
        String[] startLine = br.readLine().split(" ");

        N = Integer.valueOf(startLine[0]);
        O = Integer.valueOf(startLine[1]);

        tree = new Node[N*2];

        // input for array elements
        String[] arrayElem = br.readLine().split(" ");
        a = new int[N];
        int j = 0;
        for (String str : arrayElem) {
            a[j] = Integer.valueOf(str);
            j++;
        }

        n = a.length;

        build(a);


        for (int i = 0; i < O; i++) {
            String[] cmdElem = br.readLine().split(" ");
            char ch = cmdElem[0].charAt(0);
            int sum = Integer.valueOf(cmdElem[1]);
            int max = Integer.valueOf(cmdElem[2]);

            parser(ch, sum, max);
        }
    }
}
