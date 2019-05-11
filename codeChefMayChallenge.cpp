#include<bits/stdc++.h>

using namespace std;

int main(){
    int testCases, n, answers[1000000];
    cin>>testCases;
    vector<int> results;
    
    for(int i = 0 ; i < testCases ; i++){
        cin>>n;
        int product = 1;
        if(n == 1)  results.push(1);
        else if(n == 2) results.push(5);
        else
        for(int j = 2 ; j <= n ; j++)
            product += j + j*product;
        results.push_back(product);
        
    }
    for(int  i = 0 ; i < testCases ; i++)
        cout<<results[i]<<endl;
    
    return 0;
}
