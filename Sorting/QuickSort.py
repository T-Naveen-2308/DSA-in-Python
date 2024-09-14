'''
Quick Sort: A widely used sorting algorithm based 
            on the divide-and-conquer principle, 
            which partitions the array around a pivot 
            element and recursively sorts the sub-arrays.
'''

from random import randint

def quick_sort(arr, low, high):
    if low>=high:
        return
    pivot_index = randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    start = low
    end = high
    while start<end:
        while start<high and pivot>=arr[start]:
            start += 1
        while end>low and pivot<arr[end]:
            end -= 1
        if start<end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[low], arr[end] = arr[end], arr[low]
    quick_sort(arr, low, end-1)
    quick_sort(arr, end+1, high)

if __name__=="__main__":
    n = int(input('\nEnter the number of elements: '))
    if n==0:
        print('The list is empty.')
    else: 
        arr = list(map(int, input('\nEnter the list elements\n').split()))
        quick_sort(arr, 0, n-1)
        print(f"\nAfter sorting the list elements are\n{' '.join(map(str, arr))}\n")