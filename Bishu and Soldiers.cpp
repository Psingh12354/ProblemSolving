#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	int n,num,round,round_inp;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	sort(arr,arr+n);
	cin>>round;
	for(int i=0;i<round;i++){
		int count=0,sum=0;
		cin>>round_inp;
		int j=0; 
		while(arr[j]<=round_inp && j<n)
        {
            count++;
            sum+=arr[j];
            j++;
        }
		cout<<count<<" "<<sum<<endl;
	}
}
