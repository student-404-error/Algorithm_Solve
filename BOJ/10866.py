import sys
input = sys.stdin.readline


class Deque:
    def __init__(self) -> None:
        self.que = []

    def push_back(self, item):
        self.que.append(item)

    def push_front(self, item):
        self.que.insert(0, item)

    def front(self):
        if self.empty():
            return -1
        return self.que[0]

    def back(self):
        if self.empty():
            return -1
        return self.que[-1]

    def size(self):
        return len(self.que)

    def empty(self):
        if len(self.que) == 0:
            return 1
        return 0

    def pop_back(self):
        if not self.empty():
            data = self.que[-1]
            self.que.pop()
            return data
        return -1

    def pop_front(self):
        if not self.empty():
            data = self.que[0]
            self.que.remove(data)
            return data
        return -1


n = int(input())
deque = Deque()
for i in range(n):
    command = input().split()
    if command[0] == 'push_back':
        deque.push_back(int(command[1]))
    elif command[0] == 'push_front':
        deque.push_front(int(command[1]))
    elif command[0] == 'front':
        print(deque.front())
    elif command[0] == 'back':
        print(deque.back())
    elif command[0] == 'empty':
        print(deque.empty())
    elif command[0] == 'size':
        print(deque.size())
    elif command[0] == 'pop_front':
        print(deque.pop_front())
    elif command[0] == 'pop_back':
        print(deque.pop_back())
