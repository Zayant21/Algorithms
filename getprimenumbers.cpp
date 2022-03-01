#include<bits/stdc++.h>
using namespace std;


int main(){
int N = 15;
int j;
for ( j=2; j < N; j++) {
    for (int f = 2; f*f <= j; f++) {
        if (j % f == 0) {
            break;
        }
        else if (f+1 > sqrt(j)) {
            cout << j << " ";
        }
    }   
}


    return 0;
}