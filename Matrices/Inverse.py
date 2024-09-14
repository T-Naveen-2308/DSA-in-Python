#Inverse of a matrix program

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
 
def remaining(d, q, p=0):
    d = d[:p]+d[p+1:]
    d = [i[:q]+i[q+1:] for i in d]
    return d

def determinant(l):
    try:
        if len(l)==1:
            return l[0][0]
        if len(l)==2:
            return l[0][0]*l[1][1]-l[1][0]*l[0][1]
        s = 0
        for i in range(len(l)):
            s += ((-1)**i)*l[0][i]*determinant(remaining(l,i))
        return s
    except RecursionError:
        print('The given matrix is too big for this algorithm.')

n = input_order()
l = input_matrix(n)
k = determinant(l)
if k:
    rl = []
    for i in range(n):
        rl.append([])
        for j in range(n):
            rl[-1].append((-1**(i+j))*(determinant(remaining(l,i,j)))/k)
    for i in rl:
        for j in i:
            print(f'{j:.2f}',end='\t')
        print()
else:
    print('\nThe matrix is not invertible.')