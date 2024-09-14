'''
Heap Sort: A comparison-based sorting algorithm 
           that uses the heap data structure to 
           maintain the partially sorted valments 
           while extracting the maximum (or minimum) 
           valment repeatedly.
'''

def restore_heap_up(heap, n):
    val = heap[n]
    while n>0 and val>heap[(n-1)//2]:
        ind = (n-1)//2
        heap[n] = heap[ind]
        n = ind
    heap[n] = val
        
    
def restore_heap_down(heap, n):
    val = heap[0]
    ind = 0
    while 2*ind+1<=n:
        l = 2*ind+1
        r = l+1
        if r<=n and heap[l]<heap[r]:
            m = r
        else:
            m = l
        if val<=heap[m]:
            heap[ind] = heap[m]
            ind = m
        else:
            break
    heap[ind] = val

if __name__=="__main__":
    n = int(input('\nEnter the number of elements: '))
    if n==0:
        print('The list is empty.')
    else: 
        arr = list(map(int, input('\nEnter the list elements\n').split()))
        for i in range(n):
            restore_heap_up(arr, i)
        print(f"\nAfter building heap the list elements are\n{' '.join(map(str, arr))}")
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            restore_heap_down(arr, i-1)
        print(f"\nAfter sorting the list elements are\n{' '.join(map(str, arr))}")