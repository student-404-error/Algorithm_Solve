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
#include "string.h"

int main(){
    int set = 0;
    int commandCnt;
    scanf("%d", &commandCnt);
    char cmd[8];
    for(int i=0; i<commandCnt;i++){
        int x;
        scanf("%s", cmd);
        if(strcmp(cmd, "all") == 0){
            set |= (1<<20)-1;
            continue;
        } else if(strcmp(cmd, "empty") == 0) {
            set = 0;
            continue;
        }
        scanf("%d", &x);
        int k = 1<<(x-1);
        if(strcmp(cmd, "add") == 0){
            set |= k;
        } else if(strcmp(cmd, "remove") == 0){
            set &= ~(1<<(x-1));
        } else if(strcmp(cmd, "check") == 0){
            if((set & k) > 0){
                printf("1\n");
            } else {
                printf("0\n");
            }
        } else if(strcmp(cmd, "toggle") == 0){
            set ^= k;
        }
    }
    return 0;
}