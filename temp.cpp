#include<bits/stdc++.h>

using namespace std;

int findHCF(int a, int b){
    if (b == 0) 
        return a; 
    return findHCF(b, a % b);  
}

int main(){
    int testCases;
    cin>>testCases;
    
    for(int i = 0 ; i < testCases ; i++){
        int n,length;
        cin>>n>>length;
        int arr[length - 1];
        unordered_map<int, int> alphabetsARR;
        set<int> alphabets;
        
        for(int j = 0 ; j < length - 1 ; j++)
            cin>>arr[j];
        
        int x = findHCF(arr[0] , arr[1]);
        alphabets.insert(x);
        alphabets.insert(arr[0] / x);
        for(int j = 1 ; j < length - 1 ; j++){
            x = arr[j] / x;
            alphabets.insert(x);
        }
        set <int> :: iterator itr; int j = 0;
        for( itr = alphabets.begin() ; itr != alphabets.end() ; itr++, j++){      alphabetsARR[*itr] = j;    }
        
        char c = 'A'; 
        x = findHCF(arr[0] , arr[1]);
        /*c = c + alphabetsARR[ arr[0] / x ];
        cout<< c ;
        c = c + alphabetsARR[ x ];
        cout<<c;*/
        
        //cout<<endl<<alphabetsARR[5]<<endl;
        for(int j = 1 ; j < length - 1 ; j++){
            x = arr[j] / x;
            c += alphabetsARR[ x ];
            cout<< x <<" alphabetsARR[ x ]="<<alphabetsARR[ x ]<<" "<< c<<endl ;
        }
        
    }
    
    return 0;
}
