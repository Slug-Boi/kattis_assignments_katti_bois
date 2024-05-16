#include <iostream> 
#include <vector>

using namespace std;

// Array

vector<int> arr;


int sum_query(int l, int r) {
    int sum = 0;
    for (int i = l; i <= r-1; i++) {
        sum += arr[i];
    }
    return sum;
}

int max_query(int l, int r) {
    int max = arr[l];
    ;
    for (int i = l+1; i <= r-1; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}


int update(int pos, int value) {
    arr[pos] = value;
    return -1;
}

int parser(char ch, int n1, int n2) {
    switch (ch) {
        case 'U':
            return update(n1, n2);
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

    for (int i = 0; i < N; i++) {
        cin >> x;
        arr.push_back(x);
    }

    for (int i = 0; i < O; i++) {
        char ch;
        int n1, n2;
        cin >> ch >> n1 >> n2;
        
        int out = parser(ch, n1, n2);
        if (out != -1) {
            cout << out << endl;
        }
    }

}