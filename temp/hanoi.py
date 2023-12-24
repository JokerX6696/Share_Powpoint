#!D:/Application/python/python.exe
# 汉诺塔问题

cengshu = 3

move_counts = 0

def hanio(n,A,B,C):
    global move_counts
    if n == 1:
        print(A,"-->",C)
        move_counts += 1
    else:
        hanio(n-1,A,C,B)
        print(A,"-->",C)
        move_counts += 1
        hanio(n-1,B,A,C)


hanio(cengshu,'A','B','C')

print('需要移动的次数为 %d' %move_counts)