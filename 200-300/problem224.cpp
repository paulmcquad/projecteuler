#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
const int N = 75000000;
struct T{
    int a,b,c;
};
int main(){
    int ans=1;
    queue<T>q;
    q.push(T{2,2,3});
    while(!q.empty()){
        T t=q.front();q.pop();
        int a=t.a,b=t.b,c=t.c;
        int x=a-2*b+2*c,y=2*a-b+2*c,z=2*a-2*b+3*c;
        if(x+y+z<=N){
            ++ans;q.push(T{x,y,z});
        }
        x=-a+2*b+2*c,y=-2*a+b+2*c,z=-2*a+2*b+3*c;
        if(a!=b&&x+y+z<=N){
            ++ans;q.push(T{x,y,z});
        }
        x=2*a+b+2*c,y=a+2*b+2*c,z=2*a+2*b+3*c;
        if(x+y+z<=N){
            ++ans;q.push(T{x,y,z});
        }
    }
    printf("%d\n",ans);
}
