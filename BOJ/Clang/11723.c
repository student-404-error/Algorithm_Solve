//
// Created by 김성현 on 2023/05/09.
//
/*
 * 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
 * add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
 * remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
 * check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
 * toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
 * all: S를 {1, 2, ..., 20} 으로 바꾼다.
 * empty: S를 공집합으로 바꾼다.
*/

#include "stdio.h"
#include "stdbool.h"
#include "string.h"

void add(bool* ptr, int x){
    ptr[x] = true;
}
void rm(bool* ptr, int x){
    ptr[x] = false;
}
void check(bool* ptr, int x){
    if(ptr[x] == 1){
        printf("1\n");
    } else {
        printf("0\n");
    }
}
void toggle(bool* ptr, int x){
    if(ptr[x]){
        ptr[x] = false;
    } else {
        ptr[x] = true;
    }
}
void all(bool* ptr){
    for(int i=0;i<20;i++) {
        ptr[i] = true;
    }
}
void empty(bool* ptr){
    for(int i=0;i<20;i++) {
        ptr[i] = false;
    }
}
int main(){
    // 0 -> false
    // 1 -> true
    bool set[20] = {false,};
    int commandCnt;
    bool* ptr = &set[0];
    scanf("%d", &commandCnt);
    for(int i=0; i<commandCnt;i++){
        char cmd[8];
        int x;
        scanf("%s", cmd);
        if(strcmp(cmd, "add") == 0){
            scanf("%d", &x);
            add(ptr, x-1);
        } else if(strcmp(cmd, "remove") == 0){
            scanf("%d", &x);
            rm(ptr, x-1);
        } else if(strcmp(cmd, "check") == 0){
            scanf("%d", &x);
            check(ptr, x-1);
        } else if(strcmp(cmd, "toggle") == 0){
            scanf("%d", &x);
            toggle(ptr, x-1);
        } else if(strcmp(cmd, "all") == 0){
            all(ptr);
        } else if(strcmp(cmd, "empty") == 0){
            empty(ptr);
        }
    }
//    for(int i=0; i<20;i++) {
//        printf("%d ", set[i]);
//    }
    return 0;
}