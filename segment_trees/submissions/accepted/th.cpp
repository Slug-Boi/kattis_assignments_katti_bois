
#include <iostream>
#include <cstring>  
#include <algorithm>
#include <vector>

using namespace std;

// Arrays
vector<pair<int,int> > tree;
vector<int> a;

// length of the array
int n;

int build(vector<int> arr) {
    for (int i = 0; i < n; i++) {
        tree[n+i] = make_pair(arr[i], arr[i]);
    }

    for (int i = n-1; i > 0; i--) {
        tree[i] = make_pair((tree[i<<1].first + tree[i<<1|1].first), max(tree[i<<1].second, tree[i<<1|1].second));
    }

    return 0;
}

int updateTreeNode(int p, int value) {
    p = p+n;

    tree[p] = make_pair(value, value);


    while (p > 1) {
        tree[p >>1] = make_pair((tree[p].first + tree[p^1].first), max(tree[p].second, tree[p^1].second));
        p >>= 1;
    }

    return -1;
}

int sum_query(int l, int r) {

    int res = 0;

    l += n;
    r += n;

    while (l < r) {
        if (l & 1) {
            res += tree[l].first;
            l++;
        }

        if (r & 1) {
            r--;
            res += tree[r].first;
        }

        l >>= 1;
        r >>= 1;
    }

    return res;
}

int max_query(int l, int r) {
    int res = 0;

    l += n;
    r += n;

    while (l < r) {
        if (l & 1) {
            res = max(res, tree[l].second);
            l++;
        }

        if (r & 1) {
            r--;
            res = max(res, tree[r].second);
        }

        l >>= 1;
        r >>= 1;
    }

    return res;
}

int parser(char ch, int n1, int n2) {
    switch (ch) {
        case 'U':
            return updateTreeNode(n1, n2);
            break;
        case 'S':
            return sum_query(n1, n2);
            break;
        case 'M':
            return max_query(n1, n2);
            break;
    }
    return -1;
}

int main() {
    int N, O, x;

    cin >> N >> O;

    tree = vector<pair<int,int> >(N*2, make_pair(0,0));

    for (int i = 0; i < N; i++) {
        cin >> x;
        a.push_back(x);
    }
    
    n = a.size();

    build(a);
    
    for (int i = 0; i < O; i++) {
        char ch;
        int n1, n2;

        cin >> ch >> n1 >> n2;

        int out = parser(ch, n1, n2);

        if (out != -1) {
            cout << out << endl;
        }
    }

    return 0;
}

