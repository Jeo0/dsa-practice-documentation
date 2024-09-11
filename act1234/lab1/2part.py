"""
part 2 linked list
1 define a node class:
    - create class: Node
    - attributes: value, next
2 define linkedlist class:
    - create class: Linkedlist (manages the nodes)
    methods to implement:
        - add new node to end of list
        - delete node by its value
        - print all nodes in the list
3 test linkedlist class:
    - add a few nodes to linkedlist
    - delete some nodes from linkedlist
    - print final state of linked list
"""

""" # failure
class Node:
    def __init__(self):
        self.value = None
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = Node()

    def add(self, value):
        self.head.value = value

        index = 0
        while self.head.next is not None:
            index +=1 
        self.head.next = index

    def printlist(self):
        pass


pogi = Linkedlist()
pogi.add(10)
pogi.printlist()


# implement later when initialiizng 
# with a tuple
class Linkedlist:
    def __init__(self, *values):
        if len(values) == 0:
            print("no values")
        else:
            print("values: ", values)

    def add(self, value, tail):
        self.newnode = Node(value, tail)
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class Linkedlist:
    def __init__(self, *values):
        self.head = Node()
        self.initializer(*values)
        self.tail = None


    def add(self, value):
        """
        param:  value   

        appends only an element to the end
        returns void
        """
        new_node = Node(value)      # initialize the value first with a new node
        current = self.head         # makes the context that
                                    # we are handling the current node
                                    # while also initialize the next node regardless

        while current.next is not None:
            current = current.next
        while current.previous is not None:
            current = current.previous


        current.previous = current  # point to self
        current.next = new_node     # shift context to right

    def printlist(self):
        """
        prints things the list
        returns void
        """

        # store it in cache then traverse to the next node
        tempCache = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            tempCache.append(current_node.value)
        print(tempCache) 

        
    def deleteThis(self, index):
        """
        param:  index   

        deletes the index specified
        returns void
        """
        current_node = self.head

        # go to the node
        current_index = 0
        last_node = current_node                # set to self node
        while current_index-1 != index:
            last_node = current_node
            current_node = current_node.next
            current_index +=1
            #print("im lastly at curreeeentindex of ", current_index)
            print("last_node.value:\t", last_node.value)
            print("current_node.value:\t", current_node.value)
            print()
            
        print(":::::::::finish:::::::::::::")
        # after arriving here, delete
        print("\n===========\nbefore:")
        print("lastnode.next:\t\t", last_node.next)
        print("lastnode.value:\t\t", last_node.value)
        print("current_node.next:\t", current_node.next)
        print("current_node.value:\t", current_node.value)
        last_node.next = current_node.next

        print("\nafter")
        print("lastnode.next:\t\t", last_node.next)
        print("lastnode.value:\t\t", last_node.value)
        print("current_node.next:\t", current_node.next)
        print("current_node.value:\t", current_node.value)
        print()







    def initializer(self, *values):
        """
        param:      *values

        pass some values here to initialize the first values
        """
        if len(values) != 0:
            for iii in values:
                self.add(iii)











# operations
pogi = Linkedlist(123,345,456)
pogi.printlist()

# add multiple, then print
buffers = [909,123]
for bbb in buffers:
    pogi.add(bbb)
pogi.printlist()


# deletion
#pogi.deleteThis(2)
#pogi.deleteThis(0)
pogi.deleteThis(3)
pogi.printlist()


