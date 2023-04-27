from queue import PriorityQueue
import sys

# 속도가 빠르게 sys에 있는 함수들을 가져옴.
print = sys.stdout.write
input = sys.stdin.readline

N = int(input())

my_queue = PriorityQueue()
# 우선순위 큐 선언
for i in range(N):
    request = int(input())
    # 0이 입력되는지 숫자가 입력되는지 확인
    if request == 0:
        # 큐가 비어있는지 확인
        if my_queue.empty():
            # 0을 출력 후 줄바꿈
            print('0\n')
        else:
            temp = my_queue.get()
            # temp는 우선순위 큐에서 하나 뽑아서 출력
            print(str((temp[1]))+'\n')
    else:
        # 0이 아닌 수가 입력되면 정렬 후 큐에 할당
        my_queue.put((abs(request), request))