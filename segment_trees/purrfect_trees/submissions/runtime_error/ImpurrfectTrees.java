// This solution create a runtime error because the "tree" array gets initialised to be of size N instead of 2*N
import java.util.Scanner;

public class ImpurrfectTrees {
    private static int N, O;
    private static int n;
    private static int[] a;
    private static Node[] tree;

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
        switch (ch) {
            case 'M':
                System.out.println(maxQuery(n1, n2));
                break;
            case 'S':
                System.out.println(sumQuery(n1, n2));
                break;
            case 'U':
                updateTreeNode(n1, n2);
                break;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);  // Create a Scanner object
        System.out.println();  

        N = scan.nextInt();
        O = scan.nextInt();
        System.err.println("N: " + N + "     O: " + O);
        tree = new Node[N];

        // input for array elements
        a = new int[N];
        for (int i = 0; i < N; i++) {
            a[i] = scan.nextInt();

        }
        n = a.length;
        System.err.println("n: " + n);

        build(a);

        for (int i = 0; i < O; i++) {
            char ch = scan.next().charAt(0);
            int sum = scan.nextInt();
            int max = scan.nextInt();

            parser(ch, sum, max);
        }
    }
}
