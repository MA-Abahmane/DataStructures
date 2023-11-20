"""
    In computing, a hash table (hash map) is a data structure that implements an
associative array abstract data type, a structure that can map keys to values.
A hash table uses a hash function to compute an index, also called a hash code,
into an array of buckets or slots, from which the desired value can be found.
"""


class node:
    """ Node class """

    def __str__(self) -> str:
        return f'{self.key}: {self.val}'

    def __init__(self, key, val=None):
        """ class constructor """
        self.prev = None
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    """ Hash Table """

    def __str__(self):
        return str(self.table)


    def __init__(self, tableLen=50):
        # Create an array of N elements all containing None
        self.tableLen = tableLen
        self.table = [None] * tableLen


    def hash(self, key):
        """ The Hashing method returning the index of given value """
        return key % self.tableLen


    def push(self, key, value=None):
        """ A method that pushes values into the hash table """
        # hash the value to get the index
        idx = self.hash(key)

        # create new node and push to table
        newNode = node(key, value)

        if (self.table[idx] != None):
            crn = self.table[idx]
            while (crn.next):
                crn = crn.next

            crn.next = newNode
            newNode.prev = crn
        else:
            self.table[idx] = newNode


    def pop(self, getKey, getVal=None):
        """ removes specified element from table """

        # if only the index is given; remove all elements of that index
        if (not getVal):
            self.table[hash(getKey)] = None
        # is the index and value are both given; search for the value and remove
        else:
            crn = self.table[self.hash(getKey)]

            if (crn != None):
                if (crn.key == getKey and crn.val == getVal):
                    self.table[self.hash(getKey)] = crn.next
                    crn.mext = None

                while (crn.next):
                    crn = crn.next
                    if (crn.key == getKey and crn.val == getVal):
                        crn.prev.next = crn.next
                        if (crn.next):
                            crn.next.prev = crn.prev


    def display(self):
        """ display the hash table """

        for i in range(self.tableLen):
            if (self.table[i] != None):
                crn = self.table[i]
                print(self.hash(crn.key), crn.val)

                while (crn.next):
                    crn = crn.next
                    print(self.hash(crn.key), crn.val)


    def get(self, getKey):
        """ get value from table and return values found """
        objList = []
        crn = self.table[self.hash(getKey)]

        if (crn != None):
            objList.append([crn.key, crn.val])
            while (crn.next):
                objList.append([crn.key, crn.val])
                crn = crn.next

            return objList

        return None


    def Keydisplay(self):
        """ display the hash table as a 2d table """

        for i in range(self.tableLen):
            if (self.table[i] != None):
                crn = self.table[i]
                print(f'{crn.key}: ', end='')
                print(crn.val, end='')

                while (crn.next):
                    crn = crn.next
                    print(',' ,crn.val, end='')
                print()






ht = HashTable()

print(ht, end='\n\n')


ht.push(1)
ht.push(1)
ht.push(2)
ht.push(2, 'F2')
ht.push(2, 'F2.5')
ht.push(2, 'F2.7')

ht.push(27, 'F27')
ht.push(28, 'F28')


ht.push(49, 'F49')
ht.push(49, 'F49.9')
ht.push(5001, 'F50')

ht.display()
print()

ht.pop(1)
ht.pop(2, 'F2.5')
ht.pop(49, 'F49.9')
ht.pop(28, 'F28')

ht.Keydisplay()

print()
print(ht.get(2))
