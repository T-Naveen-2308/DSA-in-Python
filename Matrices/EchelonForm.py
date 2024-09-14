#Echelon form of a matrix

def input_order(k=True):
    while True:
        if k:
            print('\nEnter the order of the matrix : ', end = '')
            k = False
        else:
            print('\nPlease enter the order of the matrix again : ', end = '')
        try:
            n = int(input())
            if n<1:
                print('The order of the matrix cannot be less than 1.')
            else:
                return n
        except ValueError:
            print('The order must be a natural number.')

def input_matrix(n, k=True):
    while True:
        if k:
            print('\nEnter the elements of the matrix in form of a matrix')
            k = False
        else:
            print('\nPlease enter the elements of the matrix again in form of a matrix')
        try:
            l = [list(map(float, input().split())) for i in range(n)]
            if len(l[0]) != len(l):
                flag1 = True
            else:
                flag1 = False
            flag2 = False
            for i in range(1,len(l)):
                if len(l[i])!=len(l[0]):
                    flag1 = False
                    flag2 = True
                    break
            if flag1:
                print('The matrix entered is not a square matrix.')
            elif flag2:
                print('The matrix entered is not a matrix.')
            else:
                return l
        except ValueError:
            print('The elements of the matrix must be real numbers.')

def trans(r1, k, r2):
    d = []
    for i in range(len(r1)):
        d.append(r1[i]+k*r2[i])
    return d

n = input_order()
l = input_matrix(n)
for i in range(len(l)):
    if l[i][i] == 0:
        flag = True
        for k in range(i+1, len(l)):
            if l[k][i]:
                l[i], l[k] = l[k], l[i]
                flag = False
                break
        if flag:
            continue
    for j in range(i+1, len(l)):
        k = -l[j][i]/l[i][i]
        l[j] = trans(l[j], k, l[i])
for i in range(len(l)):
    k = l[i][i]
    if k:
        for j in range(len(l)):
            l[i][j] /= k
print('\nThe echelon form of the matrix is')
for i in l:
    for j in i:
        print(f'{j:.2f}', end = '\t')
    print()
print()