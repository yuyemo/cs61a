#include<stdio.h>
int double_eight(int k){
    if(k<10){
        return 0;
    }
    else{
        int last_two=k%100;
        int all_but_last=int(k/10);
        if(last_two==88){
            return 1;
        }
        else{
            return double_eight(all_but_last);
        }
    }
}
void main() {
    int date[100 * 1024 * 1024];
    date[0] = 1;
    return ;
}