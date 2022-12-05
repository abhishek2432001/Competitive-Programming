#include<bits/stdc++.h>
using namespace std;

bool is_distinct(int n){
	set<int>s;
	while(n>0){
		int rem = n%10;
		if(s.count(rem)==1)return false;
		else s.insert(rem);
		n = n/10;
	}	
	return true;
}
int main(){
	int n;
	cin>>n;
	n++;
	bool ans = is_distinct(n);
	while(!ans){
		n++;
		ans = is_distinct(n);
	}
	cout<<n;
	return n;
}

