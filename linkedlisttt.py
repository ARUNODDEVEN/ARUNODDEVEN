class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def createlist(self):
        print('Enter the choice:')
        choice = int(input(''' 
1.inset a element in beginning
2.insert a element in  last
3.insert inbetween elements
4.print
5.main
'''))
        if choice == 1:
            if self.head == None:
                element = int(input('Enter the element you want to insert:'))
                self.head = element
                self.head = Node(element)
            else:
                element = int(input('Enter the element you want to insert:'))
                temp = self.head
                self.head = Node(element)
                self.head.next = temp

        elif choice == 2:
            if self.head == None:
                print('List is already Empty:')
                exit(0)
            else:
                element = int(input('Enter the element you want to insert:'))
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = Node(element)
        elif choice == 3:
            if self.head == None:
                print('List is already Empty:')
                exit(0)
            else:
                element = int(input('Enter the element you want to insert:'))
                position = int(
                    input('Enter the element after which you want to insert the element'))
                temp = self.head
                while temp.next != None and temp.data != position:
                    temp = temp.next
                if temp.next == None:
                    print(
                        position, 'Element is not present so insertion is not posible')
                else:
                    temp2 = temp.next
                    temp.next = Node(element)
                    temp.next.next = temp2
        elif choice == 4:
            if self.head == None:
                print('list is empty')
            else:

                temp = self.head
                while temp != None:
                    print(temp.data)
                    temp = temp.next
        elif choice == 5:
            main()
        else:
            print('Enter valid statement:')
            exit(0)

    def delete(self):
        print('Enter the choie')
        choic = int(input('''
1.deletion at first
2.deletion at end
3.deletion in between
4.print 
5.Main'''))
        if choic == 1:
            if self.head == None:
                print('list is already Empty')
            else:
                self.head = self.head.next
        elif choic == 2:
            if self.head == None:
                print('List is already Emptyyy')
            else:
                temp = self.head
                temp2 = self.head.next
                while temp2.next != None:
                    temp2 = temp.next
                    temp = temp2
                temp.next = None
        elif choic == 4:
            if self.head == None:
                print('list is empty')
            else:

                temp = self.head
                while temp != None:
                    print(temp.data)
                temp = temp.next
        elif choic == 5:
            main()

        else:
            print('invalid choice')


mylist = Linked_List()


def main():
    print('Enter your choice:')
    choic = int(input(''' 
1.insert
2.deletion
0.exit
'''))
    while choic != 0:
        if choic == 1:
            mylist.createlist()
        elif choic == 2:
            mylist.delete()
        elif choic == 0:
            exit(0)
        else:
            print('invalid choice')


main()
