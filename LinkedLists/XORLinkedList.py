class Node:
    def __init__(self,data):
        self.data = data
        self.pn = 0

class XorLinkedList:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.count = 0
        self.ll = []

    def re_by_add(self, n):
        for i in self.ll:
            if id(i)==n:
                return i

    def insert_begin(self, data):
        temp = Node(data)
        self.ll.append(temp)
        if self.head:
            temp.pn = id(self.head)
            self.head.pn = id(temp)^self.head.pn
            self.head = temp
        else:
            self.head = temp
            self.tail = temp
        self.count += 1

    def insert_end(self, data):
        temp = Node(data)
        self.ll.append(temp)
        if self.head:
            temp.pn = id(self.tail)
            self.tail.pn = id(temp)^self.tail.pn
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
            self.ll.append(temp)
            temp1 = self.head
            p = 0
            t = 0
            while i<pos:
                t = id(temp1)
                temp1 = self.re_by_add(p^temp1.pn)
                p = t
                i += 1
            temp2 = self.re_by_add(temp1.pn^p)
            temp1.pn = (temp1.pn^id(temp2))^id(temp)
            temp2.pn = (temp2.pn^id(temp1))^id(temp)
            temp.pn = id(temp1)^id(temp2)
            self.count += 1
   
    def delete_begin(self):
        if self.head==0:
            print('Underflow')
        elif self.head==self.tail:
            print('Deleted', self.head.data)
            self.head = 0
            self.tail = 0
            self.count -= 1
        else:
            print('Deleted', self.head.data)
            temp = self.re_by_add(self.head.pn)
            temp.pn = temp.pn^id(self.head)
            self.head = temp
            self.count -= 1

    def delete_end(self):
        if self.head==0:
            print('Underflow')
        elif self.head==self.tail:
            print('Deleted', self.head.data)
            self.head = 0
            self.tail = 0
            self.count -= 1
        else:
            print('Deleted', self.tail.data)
            temp = self.re_by_add(self.tail.pn)
            temp.pn = temp.pn^id(self.tail)
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
            temp1 = self.head
            p = 0
            t = 0
            i = 2
            while i<pos:
                t = id(temp1)
                temp1 = self.re_by_add(p^temp1.pn)
                p = t
                i += 1
            temp = self.re_by_add(temp1.pn^p)
            print('Deleted', temp.data)
            temp2 = self.re_by_add(temp.pn^id(temp1))
            temp1.pn = (temp1.pn^id(temp))^id(temp2)
            temp2.pn = (temp2.pn^id(temp))^id(temp1)
            self.count -= 1

    def display_forward(self):
        if self.head==0:
            print('List is empty')
        else:
            print('The elements are:')
            temp = self.head
            p = 0
            t = 0
            while temp:
                print(temp.data, end = ' ')
                t = id(temp)
                temp = self.re_by_add(temp.pn^p)
                p = t
            print()
           
    def display_backward(self):
        if self.head==None:
            print('List is empty')
        else:
            print('The elements are:')
            temp = self.tail
            p = 0
            t = 0
            while temp:
                print(temp.data, end = ' ')
                t = id(temp)
                temp = self.re_by_add(temp.pn^p)
                p = t
            print()
   
    def search(self, ele):
        temp = self.head
        f = False
        i = 1
        p = 0
        t = 0
        while temp:
            if temp.data == ele:
                f = True
                break
            i += 1
            t = id(temp)
            temp = self.re_by_add(temp.pn^p)
            p = t
        if f:
            print('The element is present at index', i)
        else:
            print('The element is not present in the list.')

linked_list = XorLinkedList()

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