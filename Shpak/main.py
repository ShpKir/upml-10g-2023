from fun_input import fun_input
#     розмір масиву
n = int(input())

#     створення масиву
arr = []
fun_input(arr, n)

#for i in range(0, n):
#    arr.append(int(input()))

#     чи є нуль нулів
flag = True
calc(arr, n, flag)

#     виведення
if flag:
    print("нема")
else:
    print("є")
