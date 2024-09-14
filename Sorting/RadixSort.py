'''
Radix Sort: A non-comparative sorting algorithm 
            that sorts numbers digit by digit, 
            typically using counting sort as a 
            subroutine, suitable for sorting integers.
'''

def radix_sort(lis):
    n = len(lis)
    maxi = max(lis)
    div = 1
    while maxi:
        bucket = [[] for i in range(10)]
        for val in lis:
            rem = (val//div)%10
            bucket[rem].append(val)
        k = 0
        for i in range(10):
            for j in range(len(bucket[i])):
                lis[k] = bucket[i][j]
                k += 1
        div *= 10
        maxi /= 10

if __name__=="__main__":
    n = int(input('\nEnter the number of elements: '))
    if n==0:
        print('The list is empty.')
    else: 
        lis = list(map(int, input('\nEnter the list elements\n').split()))
        radix_sort(lis)
        print(f"\nAfter sorting the list elements are\n{' '.join(map(str, lis))}\n")