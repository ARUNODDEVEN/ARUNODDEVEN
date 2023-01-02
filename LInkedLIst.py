class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next


mylist = LinkedList()
ist = Node(10)
second = Node(2000)
third = Node(1000)
fourth = Node(283)


mylist.head = ist
ist.next = second
second.next = third
third.next = fourth


mylist.print()
