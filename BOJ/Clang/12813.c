//
// Created by 김성현 on 2023/05/12.
//

#include "stdio.h"

int main(){
    char a[100001];
    char b[100001];
    scanf("%s", a);
    scanf("%s", b);
    // AND 연산 &
    for(int i = 0; i< 100000; i++){
        if(a[i]=='1' & b[i]=='1'){
            printf("1");
        } else {
            printf("0");
        }
    } printf("\n");
    // OR 연산 |
    for(int i = 0; i< 100000; i++){
        if(a[i]=='1' | b[i]=='1'){
            printf("1");
        } else {
            printf("0");
        }
    } printf("\n");
    // XOR 연산 서로 다를 때
    for(int i = 0; i< 100000; i++){
        if(a[i] != b[i]){
            printf("1");
        } else {
            printf("0");
        }
    } printf("\n");
    // NOT A
    for(int i = 0; i< 100000; i++){
        if(a[i]=='1'){
            printf("0");
        } else {
            printf("1");
        }
    } printf("\n");
    // NOT B
    for(int i = 0; i< 100000; i++){
        if(b[i]=='1'){
            printf("0");
        } else {
            printf("1");
        }
    }
}