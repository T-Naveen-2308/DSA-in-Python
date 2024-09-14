'''
Selection Sort: An in-place comparison-based 
                sorting algorithm that repeatedly 
                selects the minimum (or maximum) 
                element from the unsorted part and 
                swaps it with the first unsorted element.
'''

def selection_sort(lis):
    n = len(lis)
    for i in range(n-1):
        mini = lis[i]
        pos = i
        for j in range(i+1, n):
            if lis[j]<mini:
                mini = lis[j]
                pos = j
        lis[i], lis[pos] = lis[pos], lis[i]

if __name__=="__main__":
    n = int(input('\nEnter the number of elements: '))
    if n==0:
        print('The list is empty.')
    else: 
        lis = list(map(int, input('\nEnter the list elements\n').split()))
        selection_sort(lis)
        print(f"\nAfter sorting the list elements are\n{' '.join(map(str, lis))}\n")