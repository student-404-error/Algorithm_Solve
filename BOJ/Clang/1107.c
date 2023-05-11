//
// Created by 김성현 on 2023/05/09.
//
#include "stdio.h"

int main(){
    int channel, breakCnt;
    int remote[10] = {
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
    };
    scanf("%d", &channel);
    scanf("%d", &breakCnt);
    for(int i = 0; i<breakCnt; i++){
        int j;
        scanf("%d", &j);
        remote[j] = -1;
    }
    if(channel == 100){ // 채널이 100이라면 채널 전환을 할 필요 없으므로 조건 분기
        printf("0");
        return 0;  // 종료
    }
    for(int i = 0; i<10; i++) {
        printf("%d, ", remote[i]);
    }
    return 0;
}