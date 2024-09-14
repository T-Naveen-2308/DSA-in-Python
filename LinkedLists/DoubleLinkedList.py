class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_begin(self, data):
        temp = Node(data)
        if self.head:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        else:
            self.head = temp
            self.tail = temp
        self.count += 1

    def insert_end(self, data):
        temp = Node(data)
        if self.head:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        else:
            self.head = temp
            self.tail = temp
        self.count += 1

    def insert_pos(self, data, pos):
        if pos<1 or pos>self.count+1:
            print('Given position is invalid.')
        elif pos==1:
            self.insert_begin(data)
        elif pos==self.count+1:
            self.insert_end(data)
        else:
            i = 2
            temp = Node(data)
            temp1 = self.head
            while i<pos:
                temp1 = temp1.next
                i += 1
            temp1.next.prev = temp
            temp.next = temp1.next
            temp1.next = temp
            temp.prev = temp1
            self.count += 1
    
    def delete_begin(self):
        if self.head==None:
            print('Underflow')
        elif self.head.next==None:
            print('Deleted', self.head.data)
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            print('Deleted', self.head.data)
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1

    def delete_end(self):
        if self.head==None:
            print('Underflow')
        elif self.head.next==None:
            print('Deleted', self.head.data)
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            print('Deleted', self.tail.data)
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
    
    def delete_pos(self, pos):
        if pos<1 or pos>self.count:
            print('Given position is invalid.')
        elif pos==1:
            self.delete_begin()
        elif pos==self.count:
            self.delete_end()
        else:
            i = 2
            temp = self.head
            while i<pos:
                temp = temp.next
                i += 1
            print('Deleted', temp.next.data)
            temp.next = temp.next.next
            temp.next.prev = temp
            self.count -= 1

    def display_forward(self):
        if self.head==None:
            print('List is empty')
        else:
            temp = self.head
            print('The elements are:')
            while temp:
                print(temp.data, end = ' ')
                temp = temp.next
            print()
            
    def display_backward(self):
        if self.head==None:
            print('List is empty')
        else:
            temp = self.tail
            print('The elements are:')
            while temp:
                print(temp.data, end = ' ')
                temp = temp.prev
            print()
    
    def search(self, ele):
        temp = self.head
        f = False
        i = 1
        while temp:
            if temp.data == ele:
                f = True
                break
            i += 1
            temp = temp.next
        if f:
            print('The element is present at index', i)
        else:
            print('The element is not present in the list.')

linked_list = DoubleLinkedList()

print('1.  Insert Begin\n2.  Insert End\n3.  Insert Position\n4.  Delete Begin\n5.  Delete End\n6.  Delete Position\n7.  Number of elements\n8.  Display Forward\n9.  Display Backward\n10. Search\n11. Exit')

while True:
    choice = int(input('\nEnter your choice: '))
    if choice==1:
        num = int(input('Enter a number: '))
        linked_list.insert_begin(num)
    elif choice==2:
        num = int(input('Enter a number: '))
        linked_list.insert_end(num)
    elif choice==3:
        pos = int(input('Enter a position: '))
        num = int(input('Enter a number: '))
        linked_list.insert_pos(num, pos)
    elif choice==4:
        linked_list.delete_begin()
    elif choice==5:
        linked_list.delete_end()
    elif choice==6:
        pos = int(input('Enter a position: '))
        linked_list.delete_pos(pos)
    elif choice==7:
        print('Number of elements in the list are', linked_list.count)
    elif choice==8:
        linked_list.display_forward()
    elif choice==9:
        linked_list.display_backward()
    elif choice==10:
        num = int(input('Enter a number: '))
        linked_list.search(num)
    elif choice==11:
        print()
        break
    else:
        print('Invalid Choice')