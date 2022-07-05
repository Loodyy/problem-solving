#include <stdio.h>

int main(){
    // 1 -> 2, 7 -> 8->19 -> 20,37 -> 38, -> 50
    //             2 + 6    2 + 6 x 3  2 + 6x6 
    int num;
    scanf("%d", &num);

    for(int i = 0;; i++){
        if(num == 1){
            printf("%d", 1);
            break;
        }
        if(2 + i*(i+1)/2 * 6 <= num && num < 2 + (i+2)*(i+1)/2 * 6){
            printf("%d", i + 2);
            break;
        } 
    } 
}