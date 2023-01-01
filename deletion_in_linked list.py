class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def lastdelete(self):
        if self.head == None:
            print("LInked list is already empty")
            exit(0)
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
    def lastinsert(self):
        if self.head == None:
            print("Linked list is empty")
            exit(0)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            element=int(input("Enter the element to be inserted at last: "))
            temp.next = Node(element)
    
    def searching(self):
        if self.head==None:
            print("Linked list is already empty")
        else:
            s=int(input('Enter the element you want to search'))
            temp=self.head
            while temp.next!=None and temp.data!=s:
                temp=temp.next
            if temp.data==s:
                print("Element is present in the list")
            else:
                print('Element is not present')
    
    def insert_in_between(self):
        if self.head==None:
            print('List is already empty so you cannot insert element after a particular element')
        else:
            element=int(input("Enter the element you want to insert"))
            ae=int(input('Enter element after you want to insert your new element'))
            temp=self.head
            while temp.next!=None and temp.data!=ae:
                temp=temp.next
            if temp.next==None:
                print('list does not have that element')
            else:
                temp2=temp.next
                temp.next=Node(element)
                temp.next.next=temp2
    
    def insert(self):
        newelement=int(input("Enter the element you want to insert:"))
        if self.head==None:
           self.head=Node(newelement)
        else:
              temp = self.head
              while temp.next != None:
                temp = temp.next
              temp.next = Node(newelement)
            
            









        

 
mylist=Linkedlist()


mylist.insert()
mylist.lastinsert()
mylist.print()
