'''
Bubble Sort: A simple comparison-based sorting 
             algorithm that repeatedly swaps 
             adjacent elements if they are in 
             the wrong order until the entire 
             array is sorted.
'''

def bubble_sort(lis):
    n = len(lis)
    for i in range(n-1):
        for j in range(n-i-1):
            if lis[j]>lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]

if __name__=="__main__":
    n = int(input('\nEnter the number of elements: '))
    if n==0:
        print('The list is empty.')
    else: 
        lis = list(map(int, input('\nEnter the list elements\n').split()))
        bubble_sort(lis)
        print(f"\nAfter sorting the list elements are\n{' '.join(map(str, lis))}\n")