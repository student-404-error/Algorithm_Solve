# N = input()
# N_num = str(input()).split('')
# print(N_num)
# # print(sum(N_num))
# # print

a = [5, 2, 3, 4, 5, 6, 9]
d = {1:0, 2:0, 3:0}
m = {1:0}
print(d.update({1:d.get(1)+1}))
print(d)
print(d.pop())
# print(sum(a))
# print(int(round(sum(a)/len(a),0)))