#include<stdio.h>
int re=0;
void main(){
    int k;
    scanf("%d",&k);
printf("%d\n",rev(k));
printf("%d",sum(k));
}


int rev(int n){
if(n/10==0){
   re=re*10+n;
   return re;
}else{
    re=re*10+n%10;
    rev(n/10);
}


}
int sum(n){
if(n/10==0){
    return n;
}else{
return n%10+sum(n/10);
}

}


