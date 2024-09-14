#determinanterminant program

def input_order(k=True):
    while True:
        if k:
            print('\nEnter the order of the matrix less than or equal to 10 : ', end = '')
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

def input_matrices(n, k=True):
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
 
def remaining(d, k):
    d = [i[:k]+i[k+1:] for i in d[1:]]
    return d

def determinant(l):
    if len(l)==1:
        return l[0][0]
    if len(l)==2:
        return l[0][0]*l[1][1]-l[1][0]*l[0][1]
    s = 0
    for i in range(len(l)):
        s += ((-1)**i)*l[0][i]*determinant(remaining(l,i))
    return s

n = input_order()
l = input_matrices(n)
k = determinant(l)
print(f'\nThe determinant of the matrix is {k:.2f}\n')