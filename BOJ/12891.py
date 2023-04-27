import sys
input = sys.stdin.readline

len_dna_str, part_str = map(int, input().split())
dna_str = list(input())
min_dna = list(map(int, input().split()))

chk_list = [0, 0, 0, 0]
count = 0
check = 0

def add_chr(x):
    global chk_list, check, min_dna
    if x == 'A':
        chk_list[0] += 1
        if chk_list[0] == min_dna[0]:
            check += 1
    elif x == 'C':
        chk_list[1] += 1
        if chk_list[1] == min_dna[1]:
            check += 1
    elif x == 'G':
        chk_list[2] += 1
        if chk_list[2] == min_dna[2]:
            check += 1
    else:
        chk_list[3] += 1
        if chk_list[3] == min_dna[3]:
            check += 1

def remove_chr(x):
    global chk_list, check, min_dna
    if x == 'A':
        if chk_list[0] == min_dna[0]:
            check -= 1
        chk_list[0] -= 1
    elif x == 'C':
        if chk_list[1] == min_dna[1]:
            check -= 1
        chk_list[1] -= 1
    elif x == 'G':
        if chk_list[2] == min_dna[2]:
            check -= 1
        chk_list[2] -= 1
    else:
        if chk_list[3] == min_dna[3]:
            check -= 1
        chk_list[3] -= 1

# chk_list[0] = chk_list[1] = chk_list[2] = chk_list[3] = 0

for i in min_dna:
    if i == 0:
        check += 1

for i in range(part_str):
    add_chr(dna_str[i])
    # print('now', chk_list[0], chk_list[1], chk_list[2], chk_list[3], check)
    # print('char : ', dna_str[i])
if check == 4:
    count += 1
for i in range(0, len_dna_str - part_str):
    j = i + part_str
    add_chr(dna_str[j])
    remove_chr(dna_str[i])
    # print('now 2', chk_list[0], chk_list[1], chk_list[2], chk_list[3], check)
    # print('char : ', dna_str[i])

    if check == 4:
        count += 1
    
    """
    하나씩 옮기면서 체크
    가장 먼저해야할 것 일단 투인덱스를 잡는다.
    i는 이미 잡혀있으니 j를 잡아야한다. 
    
    """
print(count)


