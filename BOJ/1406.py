sent = list(map(str, input()))
n = int(input())
cursor = len(sent)
a = []
for i in range(n):
    command = input()
    if command == "L":
        if len(sent) != 0:
            a.append(sent.pop())
    elif command == "D":
        if len(a) != 0:
            sent.append(a.pop())
    elif command == "B":
        if len(sent) != 0:
            sent.pop()
    elif command[0] == "P":
        sent.append(command[-1])
print("".join(sent) + "".join(reversed(a)))
