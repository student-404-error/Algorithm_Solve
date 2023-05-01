# 바구니 순서 바꾸기
# 총 N개를 가지고 있고 i번 부터 j번까지 k를 기준으로 회전
# mid mid+1 end-1 end start start+1 mid-1
# start -> start+1 -> mid-1 -> mid -> mid+1 -> end-1 -> end

n, m = map(int, input().split())
board = [i for i in range(1, n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    board[i-1:j] = board[k-1:j] + board[i-1:k-1]

print(*board)
