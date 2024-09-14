'''
Merge Sort: A divide-and-conquer sorting 
            algorithm that recursively divides 
            the array into two halves, sorts them, 
            and then merges them back into a sorted sequence.
'''

def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i, j, k = 0, 0, low
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i<len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j<len(right):
        arr[k] = right[j]
        k += 1
        j += 1

def merge_sort(arr, low, high):
    if low>=high: return
    mid = (low+high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

if __name__=="__main__":
    n = int(input('\nEnter the number of elements: '))
    if n==0:
        print('The list is empty.')
    else: 
        arr = list(map(int, input('\nEnter the list elements\n').split()))
        merge_sort(arr, 0, n-1)
        print(f"\nAfter sorting the list elements are\n{' '.join(map(str, arr))}\n")