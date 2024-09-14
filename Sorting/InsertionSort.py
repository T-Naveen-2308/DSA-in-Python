'''
Insertion Sort: A stable and adaptive sorting 
                algorithm that builds the final 
                sorted array one item at a time by 
                repeatedly inserting elements into 
                their correct positions.
'''

def insertion_sort(lis):
    n = len(lis)
    for i in range(1, n):
        j = i-1
        temp = lis[i]
        while j>=0 and temp<lis[j]:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = temp

if __name__=="__main__":
    n = int(input('\nEnter the number of elements: '))
    if n==0:
        print('The list is empty.')
    else: 
        lis = list(map(int, input('\nEnter the list elements\n').split()))
        insertion_sort(lis)
        print(f"\nAfter sorting the list elements are\n{' '.join(map(str, lis))}\n")