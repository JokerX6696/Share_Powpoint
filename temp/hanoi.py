#!D:/Application/python/python.exe
# 汉诺塔问题

cengshu = 3

move_counts = 0

def hanio(n,source, auxiliary, target):
    global move_counts
    if n == 1:
        print(source,"-->",target)
        move_counts += 1
    else:
        hanio(n-1,source='A',auxiliary='C',target='B')
        print(source,"-->",target)
        move_counts += 1
        hanio(n-1,source=auxiliary,auxiliary=source,target=target)


hanio(cengshu,source='A',auxiliary='B',target='C')

print('需要移动的次数为 %d' %move_counts)