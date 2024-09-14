class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_begin(self, data):
        temp = Node(data)
        if self.head==None:
            temp.next = self.head
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            temp.next = self.head
            self.head = temp
        self.count += 1

    def insert_end(self, data):
        temp = Node(data)
        if self.head==None:
            temp.next = self.head
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.tail.next = temp
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
            temp.next = temp1.next
            temp1.next = temp
            self.count += 1

    def delete_begin(self):
        if self.head==None:
            print('Underflow')
        elif self.head.next==self.head:
            print('Deleted', self.head.data)
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            print('Deleted', self.head.data)
            self.head = self.head.next
            self.tail.next = self.head
            self.count -= 1

    def delete_end(self):
        if self.head==None:
            print('Underflow')
        elif self.head.next==self.head:
            print('Deleted', self.head.data)
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            print('Deleted', self.tail.data)
            temp.next = self.head
            self.tail = temp
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
            self.count -= 1

    def display(self):
        if self.head==None:
            print('List is empty')
        else:
            temp = self.head
            print('The elements are:')
            while temp.next != self.head:
                print(temp.data, end = ' ')
                temp = temp.next
            print(temp.data)
    
    def search(self, ele):
        temp = self.head
        f = False
        i = 1
        while temp.next != self.head:
            if temp.data == ele:
                f = True
                break
            i += 1
            temp = temp.next
        if temp.data==ele:
            f = True
        if f:
            print('The element is present at index', i)
        else:
            print('The element is not present in the list.')

linked_list = CircularLinkedList()

print('1.  Insert Begin\n2.  Insert End\n3.  Insert Position\n4.  Delete Begin\n5.  Delete End\n6.  Delete Position\n7.  Number of elements\n8.  Display\n9.  Search\n10. Exit')

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
        linked_list.display()
    elif choice==9:
        num = int(input('Enter a number: '))
        linked_list.search(num)
    elif choice==10:
        print()
        break
    else:
        print('Invalid Choice')