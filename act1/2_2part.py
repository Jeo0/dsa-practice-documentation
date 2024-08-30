class Node():
    def __init__(self, value = None):
        self.value = value
        self.head = None
        self.tail = None

pogi1 = Node(1)
pogi2 = Node(2)
pogi3 = Node(3)

pogi1.tail = pogi2.head
pogi2.tail = pogi3.head
pogi3.tail = None

class LinkedList():
    def __init__(self):
        self.head = Node()      # none initialized

    def add(self, value):
        new_node = Node(value)
        current_node = self.head

        print()
        print("start value: ", value)

        # loop until we get to the last element 
        while new_node.head != None:
            print(current_node.head)
            print(current_node.value)
            print(current_node.tail)
            current_node.tail = new_node.head
        print(current_node.head)
        print(current_node.value)
        print(current_node.tail)

        # else
        # initialize a new node
        current_node = Node(value)
        current_node.tail = None
        print(current_node.head)
        print(current_node.value)
        print(current_node.tail)

        print("end value: ", value)

    def printlist(self):
        current_node = self.head

        # loop until we get to the last element 
        while current_node.tail != None:
            print("current_node.value: ", current_node.value)
            current_node.tail = new_node.head

noice = LinkedList()
noice.add(10)
noice.add(2323)
noice.printlist()


