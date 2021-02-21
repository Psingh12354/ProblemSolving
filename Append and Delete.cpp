#include <bits/stdc++.h>

using namespace std;

// Complete the appendAndDelete function below.
string appendAndDelete(string s, string t, int k) {
    int i=0;
    int n1=s.size();
    int n2=t.size();
    int min_len=min(n1,n2);
    for(i=0;i<min_len;i++){
        if(s[i]!=t[i]);
        break;
    }
    int count=n1+n2-2*i;
    if((k==count || k>=n1+n2) || (count%2==k%2 && count<=k)){
        return "Yes";
    }
    else{
        return "No";
    }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string t;
    getline(cin, t);

    int k;
    cin >> k;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string result = appendAndDelete(s, t, k);

    fout << result << "\n";

    fout.close();

    return 0;
}
