
class node:
    """ List Node """

    def __init__(self, data=None):
        """ Class Constructor """
        self.prev = None
        self.data = data
        self.next = None


class LinkedList:
    """ Linked List class """


    def __init__(self):
        """ Class Constructor """
        # create the head node of the list
        self.head = node()


    def addRight(self, data):
        """ Add a new node to the end of the linked list """

        # create new node
        newNode = node(data)

        # get to the last node
        crnNode = self.head
        while (crnNode.next != None):
            crnNode = crnNode.next
        # add the new node at the end
        crnNode.next = newNode
        newNode.prev = crnNode


    def addLeft(self, data):
        """ Add a new node to the beginning of the linked list """
        newNode = node(data)

        # incase of index 0
        if (self.len() == 0):
            # set as first node
            self.head.next = newNode
            newNode.prev = self.head
            return newNode

        # set new node at the beginning
        temp = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

        newNode.next = temp
        newNode.prev = self.head

        return newNode


    def len(self):
        """ Returns the length of the linked list """
        n = 0
        crnNode = self.head
        while (crnNode.next != None):
            crnNode = crnNode.next
            n+=1
        return n


    def display(self):
        """ Print out the linked list """
        crnNode = self.head
        while (crnNode.next != None):
            crnNode = crnNode.next
            print(f'-[{crnNode.data}]-', end='')
        print()


    def toArray(self):
        """ returns an array representation of the linked list """
        arr = []
        crnNode = self.head
        while (crnNode.next != None):
            crnNode = crnNode.next
            arr.append(crnNode.data)
        return arr


    def insert(self, idx=0, data=None):
        """ takes in the index and the value of the new node, then inserts a new node at the given index"""

        # make sure that the given index is correct
        if (idx < 0 or idx >= self.len()):
            raise ValueError('index out of bound')

        newNode = node(data)

        # incase of index 0
        if (idx == 0):
            temp = self.head.next
            self.head.next = newNode
            temp.prev = newNode
            # set as first node
            newNode.next = temp
            newNode.prev = self.head
            return

        i = 0
        crnNode = self.head
        while (i != idx + 1):
            crnNode = crnNode.next
            i += 1

        temp = crnNode.prev
        # check is the node has a next node
        if (crnNode.next):
            crnNode.next.prev = newNode
        crnNode.prev.next = newNode

        newNode.prev = temp
        newNode.next = crnNode

        return newNode
    





Cls = LinkedList()

print(Cls.toArray())

Cls.addLeft(4)
Cls.addLeft(1)
Cls.addRight(8)
Cls.addRight(12)

Cls.display()


Cls.insert(0, '°C')
Cls.insert(2, 2)
Cls.insert(5, 10)

Frn = LinkedList()

Frn.addRight(11)
Frn.insert(0, 22)
Frn.insert(0, 33)
Frn.addLeft(44)
Frn.insert(0, 77)
Frn.addLeft('°F')

print()

Cls.display()
print(f'Length: {Cls.len()}')
print(f'Array: {Cls.toArray()}')

print()

Frn.display()
print(f'Length: {Frn.len()}')
print(f'Array: {Frn.toArray()}')
