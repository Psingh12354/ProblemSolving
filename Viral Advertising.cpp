#include <bits/stdc++.h>

using namespace std;

// Complete the viralAdvertising function below.
int viralAdvertising(int n) {
    int shared=5,total=0,liked;
    while(n){
        liked=shared/2;
        total+=liked;
        shared=liked*3;
        n-=1;
    }
    return total;
    
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = viralAdvertising(n);

    fout << result << "\n";

    fout.close();

    return 0;
}
