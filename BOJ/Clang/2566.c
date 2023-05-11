//
// Created by 김성현 on 2023/05/06.
//
#include "stdio.h"

int main(){
    int board[9][9];
    int max = 0;
    int x = 0, y = 0;
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
	    scanf("%d", &board[i][j]);
	    if(max < board[i][j]){
	        max = board[i][j];
		x = i;
		y = j;
	    }
	}
    }
    printf("%d\n", max);
    printf("%d %d", x+1, y+1);
}
